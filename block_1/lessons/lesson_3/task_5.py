days_in_month = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31
}

# Просим пользователя ввести название месяца и переводим его в нижний регистр
month = input("Введите название месяца на английском: ").lower()

# Проверяем, есть ли такой месяц в словаре
if month in days_in_month:
    # Выводим количество дней в месяце
    print(f"В месяце {month} {days_in_month[month]} дней.")
else:
    print("Такого месяца не существует.")
