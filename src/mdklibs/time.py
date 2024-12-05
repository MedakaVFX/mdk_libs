""" mdklibs.time
 
* 時間系モジュール

Info:
    * Created : 2024-12-05 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>


Release Note:
    * LastUpdated : 2024-12-05 Tatsuya Yamagishi
"""
import datetime


#=======================================#
# Settings
#=======================================#
#=======================================#
# Funcsions
#=======================================#
def get_cur_time() -> str:
    """ 現在の時間を取得
    
    Examples:
        >>> tylibs.time.get_cur_time()
        2022-07-18 11:26:01

    """
    _dt = datetime.datetime.today()
    _result = _dt.strftime('%Y-%m-%d %H:%M:%S')

    return _result