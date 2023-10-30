# Создайте класс Bank.
# Добавьте в класс конструктор без аргументов. Создайте в конструкторе поле bank_accounts c типом dict[str, BankAccount] (словарь, где ключом является номер счёта, а значением - объект BankAccount). Изначально данное поле - пустой словарь.
# Добавьте метод open_account:
# Метод принимает один аргумент - card_holder
# Создаёт новый банковский счёт и сохраняет его в поле bank_accounts
# Возвращает (return) созданный счёт.
# Добавьте метод add_money:
# Метод принимает два аргумента: account_number и money
# Находит счёт в поле bank_accounts и прибавляет к деньгам на счету соответствующее количество денег (money).


import random

def get_random_digits(count):
    if count <= 0:
        return ""

    random_digits = [str(random.randint(0, 9)) for _ in range(count)]
    return "".join(random_digits)

class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)

#class Bank:
