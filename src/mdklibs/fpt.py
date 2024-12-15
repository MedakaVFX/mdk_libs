""" mdklibs.fpt
 
* Flow PT Python API

Info:
    * Created : 2024-12-15 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>


Release Note:
    * LastUpdated : 2024-12-15 Tatsuya Yamagishi
"""
import datetime
import functools
import webbrowser

import shotgun_api3

import mdklibs as mdk

#=======================================#
# Settings
#=======================================#


#=======================================#
# Decolator
#=======================================#
def login_required(func):
    """ FPT ログイン確認用デコレータ """

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        sg = args[0]
        logger = sg.logger

        logger.debug('UNF | [fpt Loggin required]')

        sg.login()
        
        return func(*args, **kwargs)
    return _wrapper


#=======================================#
# Functions
#=======================================#
def refine_fpt_data(fpt_entity: dict):
    """ FPT データをリファイン """

    if fpt_entity:
        _time_fields = ['created_at', 'updated_at']

        for _time_field in _time_fields:
            _dt = fpt_entity.get(_time_field)
            
            if type(_dt) == datetime.datetime:
                fpt_entity[_time_field] = _dt.strftime('%Y-%m-%d %H:%M:%S')


        return fpt_entity
        

def refine_fpt_entity_list(fpt_entity_list: list[dict]):
    """ FPT データリストをリファイン"""
    for _fpt_entity in fpt_entity_list:
        refine_fpt_data(_fpt_entity)
   
#=======================================#
# Class
#=======================================#
class Fpt:
    """ FPT用クラス
 
    ShotGrid Python APIラッパークラス
 
    Attributes:
        core (:obj:`core`): パイプラインコア
        logger (:obj:`logging.logger`): パイプラインロガー
 
    """
    def __init__(self, logger) -> None:
        self.logger = logger

        self._fpt = None

        self._project: dict = None
        self._user: dict = None

        self._url: str = None


    def exists(self):
        """  
        fpt インスタンスオブジェクトの有無。ログイン判定に使用
        """
        return self._fpt
    

    def login(
        self, url: str=None, script_name: str=None, api_key: str=None, ) -> None:
        """
        
        ShotGrid ログイン

        Args:
            url (str): ShotGrid ホーム URL
            script_name (str): Script名
            api_key (str): Script名に紐づくSgトークン
            
        """
        # CA_CERTS_PATH = self.spp.get_setting('SG_SHOTGUN_API_CACERTS')

        # if not CA_CERTS_PATH.exists():
        #     message = f'File is not found\nfile = {CA_CERTS_PATH.as_posix()}'
        #     raise FileNotFoundError(message)

        self._url = url

        self._fpt = shotgun_api3.Shotgun(
            url,
            script_name,
            api_key,
            # ca_certs=CA_CERTS_PATH.as_posix(),
        )




    #----------------------------------
    # Methods
    #----------------------------------
    def create_entity(self, entity_type: str, fpt_dict: dict) -> dict:
        fpt_dict['project'] = self._project

        if self._user:
            fpt_dict['created_by'] = self._user

        try:
            return self._fpt.create(entity_type, fpt_dict)
        
        except Exception as ex:
            self.logger.error(fpt_dict)  

            raise RuntimeError(ex)
    

    def create_version(self, fpt_dict: dict):
        """ Versionを作成

        Examples:
            >>> _sg_dict = {
            >>>     'code': _code,
            >>>     'entity': _sg_liveplate,
            >>>     'description': '',
            >>>     'sg_path_to_movie': self.get_movie(),
            >>>     'sg_path_to_frame': self.get_filepath(),
            >>>     'playlists': [sg_playlist,]
            >>> }

        """
        fpt_dict['project'] = self._project

        if self._user:
            fpt_dict['user'] = self._user

        try:
            _fpt_version = self._fpt.create('Version', fpt_dict)
        except Exception as ex:
            self.logger.error(fpt_dict)

            raise ValueError(ex)

        
        _upload_movie = self._fpt.upload(
                'Version', _fpt_version.get('id'),
                fpt_dict.get('sg_path_to_movie'),
                'sg_uploaded_movie'
        )

        return _fpt_version
    

    def get_all_assets(self, filters=None, fields=None, mytask=False) -> dict:

        if filters is None:
            filters = []

        filters.append(['project', 'is', self._project])

        self.logger.debug(filters)


        if mytask:
            filters.append(
                ['tasks.Task.task_assignees', 'is', self._user])

        return self._fpt.find('Asset', filters, fields)
    


    def get_all_projects(self, filters=None, fields=None, mytask=False) -> dict:
        """ 全てのプロジェクトを取得 """
        if filters is None:
            filters = []

        filters.extend(
            [
                ['is_demo', 'is', False],
                ['is_template', 'is', False]
            ]
        )

        
        if fields is None:
            fields = []


        if mytask:
            filters.append(
                # ['users.Task.task_assignees', 'is', self._user])
                ['users', 'is', self._user])

        return self._fpt.find('Project', filters, fields)
    

    def get_all_task_template(self, filters=None, fields=None):
        """ 全てのタスクテンプレートを取得 """
        if filters is None:
            filters = []

        if fields is None:
            fields=[]

        return self._fpt.find('TaskTemplate', filters, fields)
    

    def get_all_users(self, filters=None, fields=None) -> dict:
        """ 全てのユーザーを取得 """
        if filters is None:
            filters = []

        
        if fields is None:
            fields = []


        return self._fpt.find('HumanUser', filters, fields)
    

    def get_asset_type_list(self):
        """ アセットタイプリストを取得 """
        return self.get_field_data('Asset', 'sg_asset_type')
    

    def get_field_data(self, entity, field_name):
        _context = self._fpt.schema_field_read(
                    entity,
                    field_name=field_name,
                    project_entity=self._project)
        
        return _context[field_name]['properties']['valid_values']['value']
    

    def get_url(self) -> str:
        return self._url
    

    def open_in_web(self, entity: dict):
        _sg_url = self.get_url()
        _id = entity['id']
        _type = entity['type']

        _url = f'{_sg_url}detail/{_type}/{_id}'

        webbrowser.open(_url, new=2)


    def update(self, entity_type: str, entity_id: int, sg_dict: dict) -> dict:
        """ Shotgridのエンティティをアップデート

        Args:
            entity_type(str): エンティティタイプ名（Project, Asset, Shot, Task, Version等）
            entity_id(int): 更新したいエンティティのID
            sg_dict(dict): アップデートしたいパラメータを辞書型で設定

        Returns:
            dict: アップデートしたFPTエンティティ

        Examples:
            >>> _fpt_dict = {
            >>>    'description': 'キャラA',
            >>>    'sg_status_list': 'ip',}
            >>> _fpt_asset = fpt.update('Asset', 10658, _sg_dict)        
        """

        return self._fpt.update(entity_type, entity_id, sg_dict)

if __name__ == '__main__':
    pass
