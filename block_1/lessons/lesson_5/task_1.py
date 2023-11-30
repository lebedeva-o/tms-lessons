# Напишите функцию is_year_leap, которая принимает число (год) и возвращает True
# если год високосный (см. комментарий к слайда), False если нет.


def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# print (is_year_leap(2024))
# print(is_year_leap(1900))
# print(is_year_leap(1001))
print(is_year_leap(2020))


