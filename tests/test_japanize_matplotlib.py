import os
import unittest
import matplotlib.pyplot as plt
from matplotlib import font_manager
from japanize_matplotlib import get_font_path, get_font_ttf_path


class TestJapanizeMatplotlib(unittest.TestCase):
    def test_get_font_path(self):
        is_font_path = os.path.exists(get_font_path())
        self.assertEqual(is_font_path, True)

    def test_get_font_ttf_path(self):
        is_ttf_path = os.path.exists(get_font_ttf_path())
        self.assertEqual(is_ttf_path, True)

    def test_font_manager_ttf_path(self):
        ttf_path = font_manager.fontManager.ttflist[-1].fname
        self.assertEqual(ttf_path, get_font_ttf_path())


if __name__ == '__main__':
    unittest.main()
