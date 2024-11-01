""" モジュールの説明タイトル
 
* ソースコードの一番始めに記載すること
* importより前に記載する

Version:
    * Created : v0.0.1 2024-11-01 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>

Todo:
    TODOリストを記載
    * conf.pyの``sphinx.ext.todo`` を有効にしないと使用できない
    * conf.pyの``todo_include_todos = True``にしないと表示されない

Examples:
 
    使い方について記載

    >>> print_test ("test", "message")
        test message
 
Release Note:
    * v0.0.1 2024-11-01 Tatsuya Yamagishi
        * New
"""
global logger

VERSION = 'v0.0.1'
NAME = 'Template'



import logging
import os
import sys


try:
    from PySide6 import QtCore, QtGui, QtWidgets
except:
    from qtpy import QtCore, QtGui, QtWidgets


#=======================================#
# Settings
#=======================================#
#=======================================#
# Functions
#=======================================#
#=======================================#
# Class
#=======================================#
class testClass() :
    """クラスの説明タイトル
 
    クラスについての説明文
 
    Attributes:
        属性の名前 (属性の型): 属性の説明
        属性の名前 (:obj:`属性の型`): 属性の説明.
 
    """
    def __init__(self) -> None:
        self.version = VERSION
        self.name = NAME

    
    #----------------------------------
    # Init
    #----------------------------------

    def init_ui(self):
        """
        """
        # main_window = get_maya_main_window()

        # for child in main_window.children():
        #     print(child.__class__.__name__)
        #     if child.__class__.__name__ == self.__class__.__name__
        #         child.close()
    #----------------------------------
    # Setup
    #----------------------------------
    #----------------------------------
    # Get / Set
    #----------------------------------
    #----------------------------------
    # Methods
    #----------------------------------
 
    def print_test(self, param1, param2) :
        """関数の説明タイトル
 
        関数についての説明文
 
        Args:
            引数の名前 (引数の型): 引数の説明
            引数の名前 (:obj:`引数の型`, optional): 引数の説明.
 
        Returns:
            戻り値の型: 戻り値の説明 (例 : True なら成功, False なら失敗.)
 
        Raises:
            例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )
 
        Yields:
            戻り値の型: 戻り値についての説明
 
        Examples:
 
            関数の使い方について記載
 
            >>> print_test ('test', 'message')
               test message
 
        Note:
            注意事項などを記載
 
        """
        print('TYP | #--------------------------------#')
        print('TYP | Print test')
        print(f'{param1} {param2}')
        print('TYP | #--------------------------------#')


        logger.info('TYP | #--------------------------------#')
        logger.info(f'TYP | # > {NAME}_{VERSION}: Pring')
        logger.info('TYP | #--------------------------------#')

        logger.info(f'TYP | {NAME}_{VERSION} > trash_files')



if __name__ == '__main__':
    #-------------------------#
    # Loggerセットアップ
    #-------------------------#
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    # stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(
        '[%(levelname)s][%(name)s][%(funcName)s:%(lineno)s] %(message)s')
    )
    logger.addHandler(stream_handler)


    #-------------------------#
    # Windows
    #-------------------------#
    app = QtWidgets.QApplication(sys.argv)
 
    test_object = testClass()
    test_object.print_test('test', 'message')

    app.exec_()