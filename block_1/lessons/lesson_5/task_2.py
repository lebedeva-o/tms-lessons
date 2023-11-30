# Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает
# список, состоящий из кубов первых n натуральных чисел. То есть [1**3, 2**3, 3**3, ..., n**3].
# Обязательно использование генераторов списков.


def generate_natural_cubes(n: int) -> list:
    return [i ** 3 for i in range(1, n + 1)]
n = 7
result = generate_natural_cubes(n)
print(result)

#ФУНКЦИЯ БЕЗ ГЕНЕРАТОРА СПИСКОВ

# def generate_natural_cubes(n):
#     cubes = []
#     for i in range(1, n + 1):
#         cubes.append(i ** 3)
#     return cubes
#
# n = 5
# result = generate_natural_cubes(n)
# print(result)
