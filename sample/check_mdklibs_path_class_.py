""" mdklibs.Path クラステスト
 
* モジュールの読み込み用テストコード

Info:
    * Created : v0.0.1 2024-11-08 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>
 
Release Note:
    * v0.0.1 2024-11-08 Tatsuya Yamagishi
        * New
"""
global logger

VERSION = 'v0.0.1'
NAME = 'mdklibs_path_class_test'

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
ROOT = r'C:\Users\ta_yamagishi\temp\test'

#=======================================#
# Main
#=======================================#
if __name__ == '__main__':
    # Init Logger
    logger = mdk.get_logger()

    #----------------------------
    # パスをセットする
    _path = mdk.Path(ROOT, mkdir=True)

    print(_path)


    #----------------------------
    # パスのディレクトリを開く
    _path.open_dir()


    #----------------------------
    # ディレクトリを追加する
    _path.add_dir('users')

    
    #----------------------------
    # ディレクトリストを取得
    logger.info(f'MDK | [listdir]')
    _listdir = _path.listdir()
    for _dir in _listdir:
        logger.info(_dir)