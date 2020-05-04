[![PyPI version](https://badge.fury.io/py/japanize-matplotlib.svg)](https://badge.fury.io/py/japanize-matplotlib)
# japanize-matplotlib
matplotlib を日本語表示に対応させます

## 利用方法
matplotlibをimportした後、japanize_matplotlibをimportします。

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

## FAQ
### import japanize_matplotlib したのに日本語表示になりません [#1](https://github.com/uehara1414/japanize-matplotlib/issues/1)
import japanize_matplotlib してから matplotlib でグラフを描画するまでにフォントの設定が変わる処理が入っていると、日本語表示がなされない可能性があります。

例えば、seaborn を利用している場合であれば sns.set() などで描画フォントが seaborn のデフォルトに上書きされ、日本語表示がされなくなります。

sns.set(font="IPAexGothic") のように利用フォントに IPAexGothic を設定するか、フォント上書き後に japanize_matplotlib.japanize() を利用するなどで日本語表示できるはずです。

### import のみして利用されないコードなのでフォーマッターに消されてしまいます
リンターなどの警告が気になる・コードを消される方向けに japanize_matplotlib.japanize() メソッドの実行でも import 時と同じくフォントを設定できるようになっています。
無意味な実行になりますが、時と場合に応じて実行してください。

もしくはリンターごとに無視させる設定をすることで対応できるはずです。# noqa などで設定してください。

### なぜインストール時は japanize-matplotlib で import 時は japanize_matplotlib なのですか？
チェインケースが読みやすく好きだからです。import時にはチェインケースは利用できないのでスネークケースになっています。
