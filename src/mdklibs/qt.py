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
        

def get_hspacer():
    _hspacer = QtWidgets.QSpacerItem(
        40, 20, 
        QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Minimum
    )
    
    return _hspacer


def get_menu_from_menubar(menubar, menu_name):
    """
    メニューバーからメニューを名前で取得
    """
    _menus = menubar.findChildren(QtWidgets.QMenu)
    for _menu in _menus:
        if _menu.title() == menu_name:
            return _menu
        
    return None


def get_qaction(name: str, parent: QtWidgets.QWidget):
    """ Qt5、Qt6 互換用関数
    
    * QActionのパッケージ場所が Qt5(PySide2) と Qt6(PySide6) で異なるため
    """
    try:
        return QtGui.QAction(name, parent)
    except:
        return QtWidgets.QAction(name, parent)


def get_vspacer():
    _vspacer = QtWidgets.QSpacerItem(
        40, 20, 
        QtWidgets.QSizePolicy.Minimum,
        QtWidgets.QSizePolicy.Expanding
    )
    
    return _vspacer



#=======================================#
# Class
#=======================================#
class Splitter(QtWidgets.QSplitter):
    """ Splitter 基底クラス """
    def __init__(self, parent=None):
        super().__init__(parent)


    def init_print_signal(self):
        self.splitterMoved.connect(self.print_sizes)


    def print_sizes(self):
        print(f'{self.objectName()} {self.sizes()}')

class HSplitter(Splitter):
    """ Vertical Splitter """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setOrientation(QtCore.Qt.Horizontal)


class VSplitter(Splitter):
    """ Horizontal Splitter """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setOrientation(QtCore.Qt.Vertical)


class ComboBox(QtWidgets.QComboBox):
    """ カスタムコンボボックス
    
    Signals:
        * activated(int index) : Only User
        * currentIndexChanged(int index) : Any
    """
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
    # ----------------------------------
    # Methods
    # ----------------------------------
    def select(self, name: str):
        """ 名前でアイテムを選択 """
        num = self.findText(name)
        if num == -1:
            num = 0
            
        self.setCurrentIndex(num)


class ListWidget(QtWidgets.QListWidget):
    """ TyListWidget 基底クラス 
    
    Attributes:
        setSortingEnabled(bool)
    
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSortingEnabled(True)

    # ----------------------------------
    # Get
    # ----------------------------------
    def get_all_items(self):
        return [self.item(index) for index in range(self.count())]


    def get_name_list(self) -> list[str]:
        return [item.text() for item in self.get_all_items()]


    def get_selected_name_list(self) -> list[str]:
        return [item.text() for item in self.selectedItems()]
    
    
    # ----------------------------------
    # Set
    # ----------------------------------
    def set_editable(self):
        for _index in range(self.count()):
            _item = self.item(_index)
            _item.setFlags(_item.flags() | QtCore.Qt.ItemIsEditable)


    def set_multi_selection(self):
        self.setSelectionMode(
		        QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        

    # ----------------------------------
    # Methods
    # ----------------------------------
    def add_items(self, items: list[str]):
        _name_list = self.get_name_list()
        _name_list.extend(items)

        self.clear()
        self.addItems(sorted(list(set(_name_list))))


    def item_exists(self, value: str):
        if self.find_items(value):
            return True
        else:
            return False


    def find_items(self, value:str):
        """
        Reference form : https://doc.qt.io/qtforpython-5/PySide2/QtCore/Qt.html

        Qt.MatchExactly : Performs QVariant -based matching.
        Qt.MatchFixedString : Performs string-based matching. String-based comparisons are case-insensitive unless the MatchCaseSensitive flag is also specified.
        Qt.MatchContains : The search term is contained in the item.
        Qt.MatchStartsWith : The search term matches the start of the item.
        Qt.MatchEndsWith : The search term matches the end of the item.
        Qt.MatchCaseSensitive : The search is case sensitive.
        Qt.MatchRegExp : Performs string-based matching using a regular expression as the search term. Uses the deprecated QRegExp class. This enum value is deprecated since Qt 5.15.
        Qt.MatchRegularExpression : Performs string-based matching using a regular expression as the search term. Uses QRegularExpression . When using this flag, a QRegularExpression object can be passed as parameter and will directly be used to perform the search. The case sensitivity flag will be ignored as the QRegularExpression object is expected to be fully configured. This enum value was added in Qt 5.15.
        Qt.MatchWildcard : Performs string-based matching using a string with wildcards as the search term.
        Qt.MatchWrap : Perform a search that wraps around, so that when the search reaches the last item in the model, it begins again at the first item and continues until all items have been examined.
        Qt.MatchRecursive : Searches the entire hierarchy.
        """

        return self.findItems(value, QtCore.Qt.MatchCaseSensitive)
            

    def remove_selected(self):
        _items = self.selectedItems()

        if _items is None:
            return
        
        for _item in _items:
            self.takeItem(self.row(_item))


    def select(self, item_name):
        """ Select item by name. """
        # print(item_name)
        # raise RuntimeError('test')
    

        _items = (self.findItems(item_name, QtCore.Qt.MatchContains))           
        if _items:
            self.setCurrentItem(_items[0])





if __name__ == '__main__':
    pass
