def is_prime(number):
    if number <= 1:
        return False  # 1 и меньшие числа не являются простыми

    # Проверяем делители от 2 до квадратного корня из числа
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Если найден делитель, число не простое

    return True

# Пользовательский ввод
user_number = int(input("Введите число: "))

# Проверяем, является ли число простым и выводим результат
if is_prime(user_number):
    print("True")
else:
    print("False")
