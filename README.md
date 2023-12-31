# Discord風 絵文字入力用 IME辞書
## 概要
`:ぼおm:` と入力して `💥` と変換できるような辞書のデータです．
変換を行うときに，頭の中にある絵文字のイメージは `:boom:` なのに変換するときには `しょうとつ` と入力しなければいけないギャップに苦しんでいたため作成しました．

## 使い方
Releases から emoji.txt をダウンロードして，手持ちのマシンの IME に食わせてください．

ソースコードから自分で変換する場合，`romkan` が必要になりますので，ダウンロードをしてください．
```shell
pip3 install romkan
```

## 注意
自分用に作っただけなので色々と良くない部分があると思いますが見逃してください．

一括で変換したため，個別の変換候補の検証や保証は行っていません．

Windows 版 Google 日本語入力のみ動作を確認していますが，まあ多分ほかでも動くと思います．

## 謝辞
peaceiris 様作成の 😃 絵文字入力を日本語 🇯🇵 でするためのIME 追加辞書 📙 が発想元です．

https://github.com/peaceiris/emoji-ime-dictionary


`emojis.json` は ArkinSolomon 様のリポジトリより引用しております．そのため，本ファイルの著作権は氏に帰属します．

https://github.com/ArkinSolomon/discord-emoji-converter/blob/master/emojis.json


アルファベットをローマ字読みする変換にはromkanを使用しています．

https://github.com/soimort/python-romkan

https://pypi.org/project/romkan/


以上の3リポジトリへの contributor のみなさまに厚く御礼を申し上げます。
