# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.


import re


def get_longest_word(text: str) -> str:
    if not re.match("^[a-zA-Z\s]*$", text):
        return "Invalid characters in text. Use only english words and spaces"
    words = text.split()
    return max(words, key=len)

text = "hello this is a string with words and spaces and big big woooooooooord"
result = get_longest_word(text)
print(result)


