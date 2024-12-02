""" mdklibs.Data クラステスト
 
* モジュールの読み込み用テストコード

Info:
    * Created : v0.0.1 2024-11-10 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>
 
Release Note:
    * v0.0.1 2024-11-10 Tatsuya Yamagishi
        * New
"""
global logger

VERSION = 'v0.0.1'
NAME = 'mdklibs_data_test'

import os
import sys


os.environ['MDK_DEBUG']='1'

sys.path.append(os.path.dirname(__file__)+'/../src')
import mdklibs as mdk

#=======================================#
# Settings
#=======================================#

#=======================================#
# Main
#=======================================#
if __name__ == '__main__':
    # Init Logger
    logger = mdk.get_logger()


    