import os
import pathlib

import matplotlib
from matplotlib import font_manager

FONTS_DIR = 'fonts'
FONT_NAME = "IPAexGothic"

font_dir_path = pathlib.Path(os.path.abspath(__file__)).parent / pathlib.Path(FONTS_DIR)
font_dirs = [str(font_dir_path), ]
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)

matplotlib.rc('font', family=FONT_NAME)
