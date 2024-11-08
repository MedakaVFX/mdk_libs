""" mdklibs
 
* VFX用Pythonパッケージ

Version:
    * Created : v0.0.1 2024-11-01 Tatsuya YAMAGISHI
    * Coding : Python 3.12.4 & PySide6
    * Author : MedakaVFX <medaka.vfx@gmail.com>
 
Release Note:
    * v0.0.1 2024-11-01 Tatsuya Yamagishi
        * added: path
"""
VERSION = 'v0.0.1'
NAME = 'mdklibs'

import logging
import os

if os.environ.get('MDK_DEBUG'):
    print('MDK | ---------------------------')
    print('MDK | [ import mdklibs package]')
    print(f'MDK | {NAME} {VERSION}')
    print('MDK | ---------------------------')

#=======================================#
# Import Modules
#=======================================#
from . import file
from . import path


from .path import Path


#=======================================#
# Functions
#=======================================#
def get_logger() -> logging.Logger:
    _logger = logging.getLogger(__name__)

    if os.environ.get('MDK_DEBUG'):
        _logger.setLevel(logging.DEBUG)
    else:
        _logger.setLevel(logging.INFO)
    
    _logger.propagate = False
    _stream_handler = logging.StreamHandler()
    _stream_handler.setFormatter(logging.Formatter(
        '[%(levelname)s][%(name)s][%(funcName)s:%(lineno)s] %(message)s')
    )
    _logger.addHandler(_stream_handler)

    return _logger


def name() -> str:
    return NAME


def version() -> str:
    return VERSION