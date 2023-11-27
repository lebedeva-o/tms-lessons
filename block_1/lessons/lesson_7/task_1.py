# Пользователь вводит произвольное количество латинских букв через пробел. Буквы могут быть
# как в верхнем, так и в нижнем регистре (на результат работы это влиять не должно).
# Напишите функцию map_to_tuples, которая принимает список из этих букв и возвращает список из кортежей.
# В каждом кортеже первой должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
# Выведите результат работы функции на экран.
#
# Пример:
# Ввод пользователя: a B c
# Результат программы: [('A', 'a'), ('B', 'b'), ('C', 'c')]
#
# Используйте функции map, lower, upper


def map_to_tuples(list_data):
    return_list = list(map(lambda a: (a.upper(), a.lower()), list_data))

    return return_list


new_list = map_to_tuples(input("Enter an arbitrary number of latin letters separated by spaces: ").split())

print(new_list)