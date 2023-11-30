# Напишите функцию get_most_frequent_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.

import re
from collections import Counter


def get_most_frequent_word (text: str) -> str:
    if not re.match("^[a-zA-Z\s]*$", text):
        return "Invalid characters in text. Use only english words and spaces"
    word = text.split()
    cnt = Counter(word)
    most_frequent_word = max(cnt, key=cnt.get)
    return most_frequent_word

text = input("Enter text: ")
most_frequent_word = get_most_frequent_word(text)
print("The most frequent word is: ", most_frequent_word)
