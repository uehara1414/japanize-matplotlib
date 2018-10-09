# japanize-matplotlib
matplotlib を自動で日本語表示に対応させる

## 利用方法
import するだけ
```python
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.plot([1, 2, 3, 4])
plt.ylabel('簡単なグラフ')
plt.show()
```

## インストール
```sh
# pipenv
pipenv install japanize_matplotlib

# またはpip
pip install japanize_matplotlib
```

## 利用フォント
IPAexゴシック(Ver.003.01)
