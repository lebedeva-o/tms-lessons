# Создайте файл friends.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания
# from person import Person
# Создайте переменную my_friends - список из объектов класса Person. Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
# Выведите информацию о каждом друге на экран.
# Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter, либо генератор списков).
# Заверните код из пунктов 5 и 6 в функции get_oldest_person и filter_male_person соответственно.


from person import Person


my_friends = [
    Person('Alan East', 43, 'M'),
    Person('Rose Grey', 38, 'F'),
    Person('Ben Smit', 50, 'M')]
for friend in my_friends:
    print(friend.full_name, friend.gender, friend.age)

def get_oldest_person(friends):
    oldest_friend = max(friends, key=lambda friend: friend.age)
    return oldest_friend

oldest_friend = get_oldest_person(my_friends)
if oldest_friend:
    print("\nСамый старший друг:")
oldest_friend.print_person_info()

def filter_male_person(friends):
    male_friend = filter(lambda friend: friend.gender == "M", friends)
    return male_friend

male_friend_list = filter_male_person(my_friends)
if male_friend_list:
    print("\nИнформация о друзьях мужского пола:")
    for male_friend in male_friend_list:
        male_friend.print_person_info()