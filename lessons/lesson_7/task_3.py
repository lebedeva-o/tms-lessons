# * Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.
#
# Пример:
# Ввод пользователя: a B c d E F
# Результат программы: ['B', 'c', 'd', 'F']
#
# Используйте функцию filter.


def remove_vowels(list_data):

    a_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return_list = list(filter(lambda a: None if a in a_list else a, list_data))

    return return_list


new_list = remove_vowels(input("Enter an arbitrary number of latin letters separated by spaces: ").split())

print(new_list)