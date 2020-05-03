[![PyPI version](https://badge.fury.io/py/japanize-matplotlib.svg)](https://badge.fury.io/py/japanize-matplotlib)
# japanize-matplotlib
matplotlib を日本語表示に対応させます

## 利用方法
matplotlibをimportした後、japanize_matplotlibをimportします。

リンターの警告が気になある方向けに japanize_matplotlib.japanize() メソッドの実行でもimport時と同じくフォントを設定できるようになっています。

```python
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.plot([1, 2, 3, 4])
plt.xlabel('簡単なグラフ')
plt.show()
```


![demo](https://raw.githubusercontent.com/uehara1414/japanize-matplotlib/master/demo.png?token=AOnChuZIQchUxiL0U8qlW633FM-RMSuvks5bxW8zwA%3D%3D "demo")

## インストール
```sh
# pipenvで
pipenv install japanize-matplotlib

# またはpipで
pip install japanize-matplotlib
```

## 利用フォント
IPAフォントのIPAexゴシック(Ver.003.01)を利用しています。
利用にあたっては[IPAフォントライセンスv1.0](https://github.com/uehara1414/japanize-matplotlib/blob/master/japanize_matplotlib/fonts/IPA_Font_License_Agreement_v1.0.txt)に同意してください。
