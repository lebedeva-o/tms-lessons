# Создайте файл person.py.
# Создайте класс Person. У класса должно быть три поля: full_name, age, gender, которые должны заполняться в конструкторе.
# Будем считать что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).
# Добавьте в класс метод print_person_info, который печатает на экран строку:
# "Person: {full_name} ({gender}), {age} years old"
# Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)
# * Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно даже через год). Текущий год можно взять с помощью модуля datetime (пример).

import datetime


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age

        if gender in ('M', 'F'):
            self.gender = gender
        else:
            raise ValueError("Поле 'gender' должно быть либо 'M' (male) либо 'F' (female)")

    def print_person_info(self):
        print(f"Person: {self.full_name} ({self.gender}), {self.age} years old")

    def get_birth_year(self):
        year = 2023
        birth_year = year - self.age
        return birth_year

    def get_birth_year_actual(self):
        year_actual = datetime.datetime.now().year
        birth_year_actual = year_actual - self.age
        return birth_year_actual

# # Создание объектов
# person1 = Person("Ivan Petrov", 33, "M")
# person2 = Person("Anna Petrova", 25, "F")
#
# # Вызов методов
# person1.print_person_info()
# print(f"{person1.full_name} was born in {person1.get_birth_year_actual()}")
#
# person2.print_person_info()
# print(f"{person2.full_name} was born in {person2.get_birth_year_actual()}")
#
