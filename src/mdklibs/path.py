""" mdklibs.path
 
* path管理用モジュール
* ファイルパスは基本的にposix_pathで処理

Version:
    * Created : v0.0.1 2024-11-01 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>
 
Release Note:
    * v0.0.1 2024-11-01 Tatsuya Yamagishi
        * New
"""

import glob
import os
import pathlib
import platform
import re
import subprocess


#=======================================#
# Settings
#=======================================#
FILE_FILTER_USD = re.compile(r'.+\.(usd|usdc|usda)')
FILE_FILTER_IMAGE = re.compile(r'.+\.(bmp|gif|png|jpeg|jpg|svg|tif|tiff|exr)')
FILE_FILTER_IMAGE_SDR = re.compile(r'.+\.(bmp|gif|png|jpeg|jpg|svg|tif|tiff)')
# FILE_FILTER_IMAGE = re.compile(r'.+\.(bmp|gif|png|jpeg|jpg|svg|tif|tiff)')
FILE_FILTER_MAYA = re.compile(r'.+\.(ma|mb)')
FILE_FILTER_MEDIA = re.compile(r'.+\.(bmp|png|jpeg|jpg|svg|tif|tiff|exr|mp4|mp3|pdf|mov|mkv)')
FILE_FILTER_RAW = re.compile(r'.+\.(cr2|cr3|dng|CR2|CR3|DNG)')
FILE_FILTER_TEXT = re.compile(r'.+\.(doc|txt|text|json|py|usda|nk|sh|zsh|bat|md)')



#=======================================#
# Funcsions
#=======================================#
def as_posix(filepath: str) -> str:
    """ 
    Args:
        filepath(str): ファイルパス

    Retuns:
        str : posix_path
    """

    return pathlib.Path(filepath).as_posix()


def get_current_version_num(filepath) -> int:
    """

    <filepath> から現在のバージョン番号を取得（最大のバージョン番号）
    
    * 同じ階層内のバージョンを探索
    * ファイルパスの最後のバージョンをバージョンNoとして使用。

    Args:
        filepath (:obj:`str or pathlib.Path`): ファイルパス

    Returns:
        int: 現在のバージョン番号

    Raises:
        例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

    Examples: 
        >>> mdk.path.get_new_version('Y:/test_project/assets/v001/CharaB_Model_v001.dat')
        4

    Note:
        * ファイルパスに複数バージョンが含まれる場合、一番大きなバージョンが最大のバージョンとして扱われる。

    """
    _versions = get_versions(filepath)

    if _versions:
        _items = filepath.split(_versions[-1])
        _filepath_list = glob.glob(_items[0]+'v*')
        # result = get_version_num(filelist[-1])

        # --------
        # Updated 2024/03/12
        _version_list = [ get_version_num(_filepath)  for _filepath in _filepath_list]
        if _version_list:
            return max(_version_list)
        else:
            return 0

    else:
        return 0



def get_current_version_path(filepath) -> str:
    """

    <filepath> から最新のバージョンパスを生成

    Args:
        filepath (:obj:`str or pathlib.Path`): ファイルパス

    Returns:
        str: 最新のバージョンパス

    Raises:
        例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

    Examples: 
        >>> mdk.path.get_new_version('Y:/test_project/assets/v001/CharaB_Model_v001.dat')
        `Y:/test_project/assets/v002/CharaB_Model_v002.dat`

    Note:
        * ファイルパスに複数バージョンが含まれる場合、一番大きなバージョンが最大のバージョンとして扱われる。

    """
    _cur_num = get_current_version_num(filepath)
    _src_num = get_version_num(filepath)
    
    return version_up(filepath, _cur_num - _src_num)



def get_version_num(filepath):
    """

    <filepath> からバージョン番号を取得（最大のバージョン番号）
        - パスにバージョンが複数含まれる場合は最大値を取得

    Args:
        filepath (:obj:`str or pathlib.Path`): ファイルパス

    Returns:
        int: 現在のバージョン番号

    Raises:
        例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

    Examples: 
        >>> mdk.path.get_new_version('Y:/test_projectv002/assets_V01/v003/CharaB_Model_v0004.v001.dat')
        4

    Note:
        * ファイルパスに複数バージョンが含まれる場合、一番大きなバージョンが最大のバージョンとして扱われる。

    """
    return max(int(_version[1:]) for _version in get_versions(filepath))


def get_versions(filepath) -> list:
    """
    <filepath> に含まれるバージョンを全て取得

    Args:
        filepath (:obj:`str or pathlib.Path`): ファイルパス

    Returns:
        list: バージョンリスト

    Raises:
        例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

    Examples: 
        >>> mdk.path.get_new_version('Y:/test_project/assets/v003/CharaB_Model_v0004.v001.dat')
        ['v003', 'v0004', 'v001']
        >>> mdk.path.get_new_version('Y:/test_projectv002/assets_V01/v003/CharaB_Model_v0004.v001.dat')
        ['v003', 'v0004', 'v001']

    Note:
        * バージョンは `._/` で区切られ、小文字の `v` から始まる数字の連続

    """
    _path = as_posix(filepath)
    _items = re.split(r'[._/]+', _path)
    _result = [_item for _item in _items if re.match(r'(v\d+)', _item)]

    return _result


def open_dir(filepath):
    """
    フォルダを開く
    """
    _filepath = pathlib.Path(filepath)
    OS_NAME = platform.system()

    if _filepath.exists():
        if _filepath.is_file():
            _filepath = _filepath.parent

        if OS_NAME == 'Windows':
            cmd = 'explorer {}'.format(str(_filepath))
            subprocess.Popen(cmd)

        elif OS_NAME == 'Darwin':
            subprocess.Popen(['open', _filepath])

        else:
            subprocess.Popen(["xdg-open", _filepath])



def open_in_explorer(filepath: str):
    """
    Explorerでフォルダを開く
    """
    if os.path.exists(filepath):
        if platform.system() == 'Windows':
            filepath = str(filepath)
            filepath = filepath.replace('/', '\\')

            filebrowser = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            subprocess.run([filebrowser, '/select,', os.path.normpath(filepath)])
        
        elif platform.system() == 'Darwin':
            subprocess.call(['open', filepath])
        
        else:
            subprocess.Popen(["xdg-open", filepath])
    else:
        raise FileNotFoundError(f'File is not found.')



def version_up(filepath, num: int=1) -> str:
    """

    `filepath` の バージョンを `num` 分加算する
    
    * マイナスも対応しているが、トータルが0以下になるとバグると思う。

    Args:
        filepath (:obj: `str or pathlib.Path`): ファイルパス
        num (:obj:`int`, num=1): カウントアップ数。

    Returns:
        str: カウントアップしたパス

    Examples: 
        >>> path = 'Y:/test_projectv002/assets_V01/v003/CharaB_Model_v0004.v001.dat'
        >>> mdk.path.version_up(path, num = 2)
        `Y:/test_projectv002/assets_V01/v005/CharaB_Model_v0006.v003.dat`
        >>> path = 'Y:/test_projectv002/assets_V01/v003/CharaB_Model_v0004.v001.dat'
        >>> mdk.path.version_up(path, num = -1)
        `Y:/test_projectv002/assets_V01/v002/CharaB_Model_v0003.v000.dat`
    Note:
        注意事項などを記載

    """
    _path = as_posix(filepath)
    _versions = get_versions(_path)

    _result = _path
    
    for _version in _versions:
        _pad = len(_version[1:])
        _count = int(_version[1:])

        _new_version = 'v' + str(max(0, _count+num)).zfill(_pad)
        _result = _result.replace(_version, _new_version)

    return _result