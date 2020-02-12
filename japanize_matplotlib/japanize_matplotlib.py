import os
import pathlib

import matplotlib
from matplotlib import font_manager

FONTS_DIR = 'fonts'
FONT_NAME = "IPAexGothic"
FONT_TTF = 'ipaexg.ttf'


def japanize():
    font_dir_path = get_font_path()
    font_dirs = [str(font_dir_path)]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    font_list = font_manager.createFontList(font_files)
    font_manager.fontManager.ttflist.extend(font_list)
    matplotlib.rc('font', family=FONT_NAME)


def get_font_ttf_path():
    return get_font_path() / FONT_TTF


def get_font_path():
    return pathlib.Path(os.path.abspath(__file__)).parent / pathlib.Path(FONTS_DIR)
