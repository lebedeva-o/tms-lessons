# Пользователь вводит произвольное количество слов через пробел. Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку,
# в которой все слова из списка соединены через символ разделитель.
#
# Пример ввода пользователя:
# hello this is my string
# @
#
# Вывод программы: hello@this@is@my@string
#
# Используйте функцию reduce.

from functools import reduce


def my_join(list_data, new_separator):
    return_list = str(reduce(lambda a, b: a + new_separator + b, list_data))

    return return_list


new_list = (input("Enter an arbitrary number of words separated by spaces: ").split())
new_separator = (input("Enter separator: "))
result = my_join(new_list, new_separator)

print(result)