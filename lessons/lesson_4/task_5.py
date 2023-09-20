number = int(input("Введите произвольное число: "))
sum_of_number = 0
while number > 0:
    num1 = number % 10
    sum_of_number += num1
    number //= 10
print(f"Сумма цифр числа: {sum_of_number}")

