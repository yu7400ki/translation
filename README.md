# translation-app

⚠️ 初回起動時に、モデルのダウンロードが行われます。オフラインで利用する場合は、事前にモデルをダウンロードしてください。

また、使用するライブラリ等を合わせて、約1GBのディスク容量を消費します。

## install

### for rye users

```
git clone https://github.com/yu7400ki/translation
cd translation
rye sync
rye run translation
```

### for non-rye users

```
git clone https://github.com/yu7400ki/translation
cd translation
python -m venv .venv
source .venv/bin/activate # or .venv/Scripts/activate on Windows
pip install -r requirements.lock
python -m translation
```
or

```
python -m venv .venv
source .venv/bin/activate # or .venv/Scripts/activate
pip install git+https://github.com/yu7400ki/translation
python -m translation
```
## 謝辞

このアプリケーションは、[staka](https://staka.jp/wordpress/)様の[fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja)、[fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en)モデルおよび、requirement.lockに記載されているライブラリを利用しています。
