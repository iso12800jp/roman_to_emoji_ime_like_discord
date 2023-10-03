# 絵文字名のローマ字読みが記録されたJSONを読み取ってIME辞書形式に変換する
import json


with open("./emojis.json", "r") as emoji_file_en:
    emojis_name_list_en = list(json.load(emoji_file_en).items())

output_list = []
for emoji_pair in emoji_file_en:
    output_list.append(f":{emoji_pair[0]}\t{emoji_pair[1]}\t記号\n")

with open("./emojis_ja.json", "w") as emoji_file_ja:
    emoji_file_ja.write("output_list.join()")