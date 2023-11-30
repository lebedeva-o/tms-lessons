# Решите прошлую задачу так, чтобы ваш декоратор работал для любой функции, с любым количеством параметров. А также чтобы работало с именованными параметрами.
# Подсказка: используйте *args и **kwargs.
#
# Пример кода программы, использующей ваш декоратор и ожидаемый вывод программы находится комментарии к слайду.


def my_decorator(func):
    def updated_func(*arg, **kwargs):
        print(f'Функция получила на вход значение {func.__name__}: {arg}, {kwargs}')
        result = func(*arg, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        return result

    return updated_func


@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d


y = my_func(1, 2, d=3, c=4)
print(f'y = {y}')