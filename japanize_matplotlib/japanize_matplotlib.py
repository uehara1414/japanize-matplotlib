import os

import matplotlib
from matplotlib import font_manager
from distutils.version import LooseVersion

FONTS_DIR = 'fonts'
FONT_NAME = "IPAexGothic"
FONT_TTF = 'ipaexg.ttf'


def japanize():
    font_dir_path = get_font_path()
    font_dirs = [font_dir_path]
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    is_support_createFontList = LooseVersion(matplotlib.__version__) < '3.2'
    if is_support_createFontList:
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
    else:
        for fpath in font_files:
            font_manager.fontManager.addfont(fpath)
    matplotlib.rc('font', family=FONT_NAME)


def get_font_ttf_path():
    return os.path.join(get_font_path(), FONT_TTF)


def get_font_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), FONTS_DIR))


japanize()
