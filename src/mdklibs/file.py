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
import csv
import urllib.request
import json
import os
import pathlib
import platform
import subprocess


#=======================================#
# Settings
#=======================================#


#=======================================#
# Funcsions
#=======================================#
#=======================================#
# I/O
#=======================================#
def open_file(filepath):
    """ <filepath>をOSで開く """
    if os.path.isfile(filepath):

        if platform.system() == 'Windows':
            cmd = 'explorer {}'.format(filepath.replace('/', '\\'))
            subprocess.Popen(cmd)
        
        elif platform.system() == 'Darwin':
            subprocess.call(['open', filepath])
        
        else:
            subprocess.Popen(["xdg-open", filepath])

    else:
        raise TypeError('"filepath" is not file.')
    

#----------------------------
# CSV
#----------------------------
def load_csv(filepath) -> dict:
    """ CSVファイルを開く """
    _result = []

    with open(filepath, 'r') as _f:
        _reader = csv.reader(_f)
        _header = next(_reader)

        for _row in _reader:
            _value = {}
            for _name, _data in zip(_header, _row):
                try:
                    _value[_name] = _data.encode()
                except:
                    _value[_name] = _data

            #print(value)
            _result.append(_value)

    return _result

def save_csv(filepath, data: list[str]):
    """ CSVファイルを保存する """
    with open(filepath, 'w') as _f:
        _writer = csv.writer(_f, lineterminator='\n') # 改行コード（\n）を指定しておく
        _writer.writerows(data)



#----------------------------
# JSON
#----------------------------
def load_json(json_file_path: str) -> dict:
    """
    Windows版 Blender 対策でencodeを'cp932'に。
        * Blender依存なのか？Python 3.10のせいか？理由は不明

        
    Todo:
        * CP932がDOS用のJISコードであるため、将来的にOS判定が必要かも by Yamagishi

    """
    try:
        with open(json_file_path, encoding='UTF-8') as f:
            result = json.load(f)

        return result

    except:
        with open(json_file_path, encoding='CP932') as f:
            result = json.load(f)

        return result


#----------------------------
# TEXT
#----------------------------
def load_lines(filepath) -> list:
    """
    <file_path> のテキストをlinesで開く
    """
    with open(filepath, encoding='utf8', errors='ignore') as _f:
        _result = _f.readlines()

    return _result



def load_text(filepath):
    return pathlib.Path(filepath).read_text(encoding='utf8')



def replace_text(filepath: str, replace_list: list[str]):
    """ 
    
    Args:
        replcae_list(list): 置き換える文字リスト（['test', 'hoge'], ['moji', 'string']）
    """
    _lines = load_lines(filepath)

    # pprint.pprint(_lines)

    for _i, _line in enumerate(_lines):
        for _replace in replace_list:
            _src, _dst = _replace

            if _src in _line:
                _src_text = f'{_i}: {_line}'
                _line = _line.replace(_src, _dst)
                _dst_text = f'{_line}'

                print(f'{_src_text} => {_dst_text}')

            _lines[_i] = _line

    save_lines(filepath, _lines)

    


def save_json(json_file_path: str, dict_data: dict):
    """
    Jsonファイルの保存

    Args:
        json_file_path (str): 保存先
        dict_data (dict): 保存するデータ
    """
    with open(json_file_path, 'w', encoding='UTF-8') as f:
        json.dump( dict_data, f, indent=4, sort_keys=True, ensure_ascii=False)


def save_lines(filepath, lines: list[str]):
    """
    lines を <file_path> で保存

    Args:
        * lines<list> : 文字列リスト
    """

    with open(filepath, mode='w', encoding='utf8') as _f:
        _f.writelines(lines)


def save_text(filepath, data):
    _path = pathlib.Path(filepath)
    _path.parent.mkdir(parents=True, exist_ok=True)
    _path.write_text(data, encoding='utf8')




#----------------------------
# Image
#----------------------------
def save_image_from_url(url, image_filepath):
    """ urlで指定された画像ファイルを保存する """
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(image_filepath, mode='wb') as local_file:
                local_file.write(data)
                
    except urllib.error.URLError as ex:
        raise urllib.error.URLError(ex)