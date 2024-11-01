""" モジュールインポートテスト
 
* モジュールの読み込み用テストコード

Version:
    * Created : v0.0.1 2024-11-01 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>
 
Release Note:
    * v0.0.1 2024-11-01 Tatsuya Yamagishi
        * New
"""
global logger

VERSION = 'v0.0.1'
NAME = 'mdk_import'

import logging
import os
import sys


os.environ['MDK_DEBUG']='1'


sys.path.append(os.path.dirname(__file__)+'/../src')
import mdklibs as mdk


#=======================================#
# Settings
#=======================================#
MDK_FILEPATH = r'c:\users\t-yamagishi\task\versions\v01\task_v002\task_v0003.ma'

#=======================================#
# Main
#=======================================#
if __name__ == '__main__':
    # Init Logger
    logger = mdk.get_logger()
    

    logger.info(f'MDK | {MDK_FILEPATH=}')
    logger.info(mdk.path.as_posix(MDK_FILEPATH))
    _versions = mdk.path.get_versions(MDK_FILEPATH)
    _max_version_num = mdk.path.get_version_num(MDK_FILEPATH)
    logger.info(_versions)
    logger.info(f'{_max_version_num}')
    logger.info(mdk.path.get_current_version_path(MDK_FILEPATH))
    logger.info(mdk.path.get_current_version_num(MDK_FILEPATH))
    logger.info(mdk.path.version_up(MDK_FILEPATH))
