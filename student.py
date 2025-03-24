class Student:
    # атрибуты класса (общие для всех объектов)
    def __init__(self, name, age, student_id, grades, major):
        self.name = name  # (строка) - имя студента.
        self.age = age  # (целое число) - возраст студента
        self.student_id = student_id # (строка) - уникальный идентификатор студента
        self.grades = grades   # (список) - список оценок студента.
        self.major = major   #   (строка) - специальность студента
    # методы объекта
    def add_grade(self, grade): # метод для добавления новой оценки в список
        self.grades.append(grade)

    def get_average_grade(self): # метод для вычисления средней оценки студента
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def  description(self): # - метод, который возвращает строку с информацией о студенте
                            # (имя, возраст, специальность, средняя оценка).
        average_grade = self.get_average_grade()
        info_student = {
            'Имя': self.name,
            'Возраст': self.age,
            'Специальность': self.major,
            'Средняя оценка': average_grade
        }
        return info_student

    def is_passing(self): # метод, который возвращает True, если средняя оценка больше или
                          # равна 4.5, и False в противном случае
        return self.get_average_grade() >= 4.5


student_1 = Student(name='Masha', age=18, student_id='1', grades=[5,4,5,5], major='python')
print(student_1.get_average_grade())
student_1.add_grade(5)
student_1.add_grade(5)
print(student_1.description())
print(student_1.is_passing())

