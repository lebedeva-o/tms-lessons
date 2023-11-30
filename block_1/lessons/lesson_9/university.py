# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count


from student import Student

students = [
    Student('Bob Porter', 5.7),
    Student('Rose Grey', 7.8),
    Student('Ben Smit', 8),
    Student('Anna Vox', 9.2)]


def calc_sum_scholarship(all_students):
    sum_scholarship = sum(student.get_scholarship() for student in all_students)
    return sum_scholarship

total_scholarship = calc_sum_scholarship(students)
print("Суммарная стипендия для всех студентов:", total_scholarship, "рублей")

def get_excellent_student_count(excellent_student):
    excellent_student_count = sum(student.is_excellent() for student in excellent_student)
    return excellent_student_count

excellent_count = get_excellent_student_count(students)
print("Количество отличников:", excellent_count)