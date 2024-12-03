""" mdklibs.data
 
* データ管理用モジュール

Info:
    * Created : 2024-11-10 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>


Release Note:
    * LastUpdated : 2024-11-10 Tatsuya Yamagishi
"""

import dataclasses
import pprint

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except:
    from qtpy import QtCore, QtGui, QtWidgets

import mdklibs as mdk
#=======================================#
# Settings
#=======================================#


#=======================================#
# Funcsions
#=======================================#
def create_menu(view, menu_name):
    _main_menu = view.menuBar()

    if _main_menu:
        _menu = get_menu_from_menubar(view.menuBar(), menu_name)

        if _menu:
            return _menu
        
        else:
            _menu = QtWidgets.QMenu(_main_menu)
            _menu.setTitle(menu_name)
            _main_menu.addAction(_menu.menuAction())

            return _menu
        

def get_qaction(name: str, parent: QtWidgets.QWidget):
    """ Qt5、Qt6 互換用関数
    
    * QActionのパッケージ場所が Qt5(PySide2) と Qt6(PySide6) で異なるため
    """
    try:
        return QtGui.QAction(name, parent)
    except:
        return QtWidgets.QAction(name, parent)
    


def get_menu_from_menubar(menubar, menu_name):
    """
    メニューバーからメニューを名前で取得
    """
    _menus = menubar.findChildren(QtWidgets.QMenu)
    for _menu in _menus:
        if _menu.title() == menu_name:
            return _menu
        
    return None


#=======================================#
# Class
#=======================================#

if __name__ == '__main__':
    pass
