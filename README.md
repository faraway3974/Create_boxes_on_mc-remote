# Create boxes on mc-remote

## 箱を作るAPI

---

このAPIでは、縦、横、高さ、角度などを入力すると自由自在に箱を生成できます。

---

# 使い方

`sample_code.py`で簡単に試すことができます。

--

例
```python
Box1 = CreateBox(10, 63, 10, 5, 3, 5, 20, 45, 0, block=block.DIAMOND_BLOCK)
Box1.create_box(mc, hollow=True)
```

(原点x, 原点y, 原点z, x方向の長さ, y方向の長さ, z方向の長さ, X軸回転角度, Y軸回転角度, Z軸回転角度, ブロックの種類)

という順で数値を書き込むとそのとおりに箱が置かれます。
```python
Box1 = CreateBox(sx, sy, sz, lx, ly, lz, rx, ry, rz, block)
Box1,create_box(mc, hollow)
```

--

## 角度の指定について

`rx, ry, rz`はそれぞれX軸・Y軸・Z軸まわりの回転角度で、度数法(0〜360)で指定します。省略すると`0`扱いになります。

正の角度を指定したときの回転方向は以下の通り(右手系)。

- `rx`: y軸 → z軸 の向き
- `ry`: z軸 → x軸 の向き
- `rz`: x軸 → y軸 の向き

思ってた向きと逆に回った場合は、角度をマイナスにすれば逆回転します。

回転の軸は原点`(sx, sy, sz)`です。

--

## 中空(hollow)オプション

`create_box`メソッドの引数に`hollow=True`を渡すと、箱の表面だけにブロックを置き、内部を空洞にできます。

```python
Box1.create_box(mc, hollow=True)
```

見た目は変わらないままブロック数を大幅に減らせるので、大きな箱を作るときの処理時間を短縮できます(辺の長さのオーダーが3乗→2乗になるイメージ)。
