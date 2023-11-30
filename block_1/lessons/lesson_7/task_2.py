# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
#
# Пример:
# Ввод пользователя: a b c d e f
# Результат программы: ['b', 'c', 'd', 'f']
#
# Используйте функцию filter.
# Список всех гласных английского языка: a, e, i, o, u


def remove_vowels(list_data):

    a_list = ['a', 'e', 'i', 'o', 'u']
    return_list = list(filter(lambda a: None if a in a_list else a, list_data))

    return return_list

new_list = remove_vowels(input("Enter an arbitrary number of latin letters separated by spaces: ").split())

print(new_list)


