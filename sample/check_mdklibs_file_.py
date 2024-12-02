""" mdklibs.file モジュールテスト
 
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
NAME = 'mdklibs_file_test'

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
ROOT = r'C:\Users\ta_yamagishi\temp'
CSV_FILEPATH = rf'{ROOT}\data.csv'
DICT_DATA = {
    'Aida': 18,
    'Suzuki': 35,
    'Yamada': 24,
    'yamagishi': 20,
}
FILEPATH = rf'{ROOT}\pic001.png'
JSON_FILEPATH = rf'{ROOT}\json_file.json'
REPLACE_LIST = [['Yamagishi', 'Tanaka'], ['YYYY', '2024'], ['MM/DD', '11/07'],]
URL_IMAGE = r'https://avatars.githubusercontent.com/u/174575702?v=4'
TEXT_DATA = 'Tatsuya Yamagishi\nYYYY/MM/DD'
TEXT_FILEPATH = rf'{ROOT}\readme.txt'

#=======================================#
# Main
#=======================================#
if __name__ == '__main__':
    # Init Logger
    logger = mdk.get_logger()

    #----------------------------
    # URLで指定されたファイルを保存する
    logger.info('MDK | [Downloag Image]')
    logger.info(f'MDK | image={URL_IMAGE}')
    logger.info(f'MDK | save={FILEPATH}')
    mdk.file.save_image_from_url(URL_IMAGE, FILEPATH)


    # OSでファイルを開く
    logger.info(f'MDK | [Open File]')
    logger.info(f'MDK | file={FILEPATH}')
    mdk.file.open_file(FILEPATH)

    
    #----------------------------
    # データをJsonファイルで保存
    _val = input('[Next > Json] Press Any Key')
    
    logger.info(f'MDK | [Save Json]')
    logger.info(f'MDK | data={DICT_DATA}')
    mdk.file.save_json(JSON_FILEPATH, DICT_DATA)

    # ファイルをエクスプローラで開く
    mdk.path.open_in_explorer(JSON_FILEPATH)

    # Jsonファイルを開く
    _data = mdk.file.load_json(JSON_FILEPATH)  
    pprint.pprint(_data)


    #----------------------------
    # データをTextファイルで保存
    _val = input('[Next > Text] Press Any Key')


    logger.info(f'MDK | [Save Text]')
    logger.info(f'MDK | data={TEXT_DATA}')

    # テキストをファイルで保存
    mdk.file.save_text(TEXT_FILEPATH, TEXT_DATA)

    
    # ファイルをエクスプローラで開く
    mdk.path.open_in_explorer(TEXT_FILEPATH)

    # Text ファイルのディレクトリを開く
    _data = mdk.path.open_dir(TEXT_FILEPATH)
    logger.info(f'MDK | text = {_data}')


    #----------------------------
    # テキストファイルの文字列を置き換え
    _val = input('[Next > Replace Text] Press Any Key')

    mdk.file.replace_text(TEXT_FILEPATH, REPLACE_LIST)
    mdk.file.open_file(TEXT_FILEPATH)


    #----------------------------
    # CSVファイル保存
    _val = input('[Next > CSV] Press Any Key')

    _keys = list(DICT_DATA.keys())
    _values = list(DICT_DATA.values())

    _data = [_keys, _values]

    # CSVで保存
    logger.info(f'MDK | data = {_data}')
    mdk.file.save_csv(CSV_FILEPATH, _data)

    # CSVを開く
    mdk.file.open_file(CSV_FILEPATH)

    # CSVのデータを開く
    _csv = mdk.file.load_csv(CSV_FILEPATH)
    logger.info(f'MDK | csv = {_csv}')