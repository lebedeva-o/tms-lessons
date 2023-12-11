import json


def test_convert_to_json():
    with open("HW_Files.txt", "r", encoding="utf-8") as file:
        text = file.read().splitlines()

    dict_txt = {}

    for line in text:
        key, value = line.split(",", 1)
        dict_txt[key] = value

    with open("HW.json", "w", encoding="utf-8") as json_file:
        data = json.dumps(
            dict_txt,
            ensure_ascii=False,
            sort_keys=True,
            indent=4)
        json_file.write(data)
