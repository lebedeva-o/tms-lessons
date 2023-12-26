# С использованием библиотеки sqlite3 выполнить следующее
# 1. Создать базу данных, в которой есть таблица Gryffindor
# 2. В таблице есть столбцы first_name, last_name, blood_status, born. Все имеют тип text, кроме последнего - int
# 3. Заполнить данными
# Harry Potter Half-blood 1980
# Ronald Weasley Pure-blood 1979
# Hermione Granger Muggle-born 1979
# Neville Longbottom Pure-blood 1980
# Rubeus Hagrid Half-breed 1928
# 4. Написать тесты, которые:
# - находят всех, родившихся в 1980м году
# - найти, кто родился раньше всех
# - добавляют волшебника со случайными данными и проверяют его наличие в базе. Потом можно его удалить
# === Со звёздочкой ===
# - найти всех, кто не родился в 1980м году
# - найти всех полукровок (полукровка - рожденный от магла ИЛИ от другого вида ;))


#ЗАДАНИЕ СДЕЛАНО В СКРИПТОВОМ ВАРИАНТЕ. выглядит не очень, но пока так (:

import sqlite3

from dataclasses import dataclass

DB_NAME = "faculty.db"
TABLE_NAME = "Gryffindor"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()

    return conn, curs


def create_table(conn, curs):
    curs.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ("
                 "first_name text,"
                 "last_name text,"
                 "blood_status text,"
                 "born int"
                 ");"
                 )
    conn.commit()


def connect_to_db():
    return create_database()


def data_for_db():
    people = [
        ('Harry', 'Potter', 'Half-blood', 1980),
        ('Ronald', 'Weasley', 'Pure-blood', 1979),
        ('Hermione', 'Granger', 'Muggle-born', 1979),
        ('Neville', 'Longbottom', 'Pure-blood', 1980),
        ('Rubeus', 'Hagrid', 'Half-breed', 1928)
    ]
    return people


def write_to_db(conn, curs, sql_request):
    curs.execute(sql_request)
    conn.commit()


@dataclass
class Persons:
    first_name: str
    last_name: str
    blood_status: str
    born: int


def main():
    conn, curs = connect_to_db()
    create_table(conn, curs)
    data = data_for_db()
    for line in data:
        write_to_db(conn, curs, f"insert into {TABLE_NAME} values {line};")
    rows = curs.execute(f"select * from {TABLE_NAME};").fetchall()
    people = [Persons(*row) for row in rows]

    for person in people:
        if person.born == 1980:
            print(f"People who were born in 1980: "
                  f"{person.first_name} {person.last_name}, {person.born}")

    earliest_person = None

    for person in people:
        if earliest_person is None or person.born < earliest_person.born:
            earliest_person = person

    if earliest_person is not None:
        print(f"Earliest birthday: \n"
              f"{earliest_person.first_name} {earliest_person.last_name}, {earliest_person.born}")

    for person in people:
        if person.born != 1980:
            print(f"People who were not born in 1980: "
                  f"{person.first_name} {person.last_name}, {person.born}")

    for person in people:
        if person.blood_status != "Pure-blood":
            print(f"Half-blood: "
                  f"{person.first_name} {person.last_name}, {person.born}")



if __name__ == '__main__':
    main()
