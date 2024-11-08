""" mdklibs.Path クラステスト
 
* パスエクスプレッション確認用モジュール

Version:
    * Created : v0.0.1 2024-11-08 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>
 
Release Note:
    * v0.0.1 2024-11-08 Tatsuya Yamagishi
        * New
"""
global logger

VERSION = 'v0.0.1'
NAME = 'mdklibs_path_context'

import logging
import os
import pprint
import sys


os.environ['MDK_DEBUG']='1'

sys.path.append(os.path.dirname(__file__)+'/../src')
import mdklibs as mdk

#=======================================#
# Settings
#=======================================#
ROOT = r'C:\Users\ta_yamagishi\temp\show'

VARS = {
    'ROOT': ROOT,
    'ASSET':'CharaA',
    'TASK': 'modeling',
    'ELEMENT': 'head',
    'DEP': '3d',
    'EXT': '.mb',
}


EXPR = r'{ROOT}/assets/{ASSET}/publish/{TASK}/%new_version%/{&asset_scene}_%new_version%.{1}'
EXPRS = {
    'asset_scene': r'{ASSET}_{TASK}_{ELEMENT}',
    'shot_code': r'{EPI}_{SEQ}_{SHOT}',
    'shot_scene': r'{EPI}_{SEQ}_{SHOT}_{TASK}',
}
#=======================================#
# Main
#=======================================#
if __name__ == '__main__':
    # Init Logger
    logger = mdk.get_logger()


    #----------------------------
    # パスをセット&作成
    _path = mdk.Path(ROOT, mkdir=True)
    print(_path)

    # バージョン桁数をセット
    _path.set_version_digits(4)

    #----------------------------
    # エクスプレッションをセット
    _path.set_exprs(EXPRS)

    #----------------------------
    # 変数をセット
    _path.set_vars(VARS)

    #----------------------------
    # エクスプレッションを評価
    _expr = r'{ROOT}/assets/{ASSET}/publish/{TASK}/%new_version%/{&asset_scene}_%new_version%{EXT}'
    _result = _path.eval(_expr)
    print(_result)
    # C:/Users/ta_yamagishi/temp/show/assets/CharaA/publish/modeling/v0001/CharaA_modeling_head_v0001.mb


    _expr = r'{ROOT}/assets/{ASSET}/publish/{TASK}/%new_version%/{&asset_scene}_%new_version%.{1}'
    _result = _path.eval(_expr, 'ma',)
    print(_result)
    # C:/Users/ta_yamagishi/temp/show/assets/CharaA/publish/modeling/v0001/CharaA_modeling_head_v0001.ma


    # 0はexpressionで使用
    _expr = r'{1}_{2}_{3}'
    _result = _path.eval(_expr, 'test', 'hogehoge', '%new_version%')
    print(_result)
    # test_hogehoge_v0001


    _path.set_var('SHOW', 'PRJ')
    _path.set_var('EPI', 'ep0')
    _path.set_var('SEQ', '010')
    _path.set_var('SHOT', '0020')
    _path.set_var('TASK', 'comp')
    _path.set_var('EXT', '.nk')
    _expr = r'{ROOT}/{SHOW}/shots/{EPI}_{SEQ}/{SHOT}/{&shot_scene}_%new_version%{EXT}'
    _result = _path.eval(_expr)
    print(_result)
    # C:/Users/ta_yamagishi/temp/show/PRJ/shots/ep0_010/0020/ep0_010_0020_comp_v0001.nk


    _expr = r'{ROOT}/{SHOW}/dailies/dailies_{DEP}_{YYYY}{MM}{DD}'
    _result = _path.eval(_expr)
    print(_result)
    # C:\Users\ta_yamagishi\temp\show/PRJ/dailies/dailies_3d_20241108