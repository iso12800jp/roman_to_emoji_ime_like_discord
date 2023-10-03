import json
import romkan


with open("./emojis.json", "r") as emoji_file_en:
    emojis_name_list_en = list(json.load(emoji_file_en).items())

print(emojis_name_list_en)

emoji_name_dic_ja = {}
for emoji_name_en in emojis_name_list_en:
    emoji_name_ja = romkan.to_hiragana(emoji_name_en[0])
    emoji = emoji_name_en[1]
    emoji_name_dic_ja[emoji_name_ja] = emoji

print(emoji_name_dic_ja)

with open("./emojis_ja.json", "w") as emoji_file_ja:
    json.dump(emoji_name_dic_ja, emoji_file_ja, indent = 4, ensure_ascii=False)