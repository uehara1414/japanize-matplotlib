import os
import unittest
import matplotlib.pyplot as plt
from japanize_matplotlib import get_font_path, get_font_ttf_path


class TestJapanizeMatplotlib(unittest.TestCase):
    def test_get_font_path(self):
        is_font_path = os.path.exists(get_font_path())
        self.assertEqual(is_font_path, True)


if __name__ == '__main__':
    unittest.main()
