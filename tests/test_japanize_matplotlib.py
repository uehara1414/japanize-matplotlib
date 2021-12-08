import os
import matplotlib.pyplot as plt
from matplotlib import font_manager
from japanize_matplotlib import get_font_path, get_font_ttf_path


def test_get_font_path():
    is_font_path = os.path.exists(get_font_path())
    assert is_font_path is True


def test_get_font_ttf_path():
    is_ttf_path = os.path.exists(get_font_ttf_path())
    assert is_ttf_path is True


def test_font_manager_ttf_path():
    ttf_path = font_manager.fontManager.ttflist[-1].fname
    assert ttf_path == get_font_ttf_path()
