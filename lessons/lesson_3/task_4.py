input_string = input("Введите произвольную строку: ")

# Используем множество (set) для хранения уникальных символов
unique_chars = set(input_string)

# Преобразуем множество обратно в кортеж
unique_chars_tuple = tuple(unique_chars)

# Выводим результат
print("Кортеж из уникальных символов:", unique_chars_tuple)
