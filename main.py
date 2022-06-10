# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
            self.finished_courses.append(course_name)

    def rate_lecturer(self, course, lecturer, points):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.eval_points:
                lecturer.eval_points[course] += [points]
            else:
                lecturer.eval_points[course] = [points]
        else:
            return 'Ошибка'

    def average_grade(self):
        grade_sum = 0
        grade_count = 0
        for grade in self.grades.values():
            grade_sum += sum(grade)
            grade_count += len(grade)
        return round(grade_sum / grade_count, 2)

    def __str__(self):
        avg_res = self.average_grade()
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_res}\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.average_grade() == other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.eval_points = {}

    def average_point(self):
        eval_sum = 0
        eval_count = 0
        for eval in self.eval_points.values():
            eval_sum += sum(eval)
            eval_count += len(eval)
        return round(eval_sum / eval_count, 2)

    def __str__(self):
        avg_res = self.average_point()
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекцииЮ {avg_res}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.average_point() < other.average_point()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.average_point() == other.average_point()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.add_courses('Python')
best_student.add_courses('Java')

best_student1 = Student('Ruoy1', 'Eman1', '1your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.add_courses('Python')

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades)

cool_mentor.rate_hw(best_student1, 'Python', 7)
cool_mentor.rate_hw(best_student1, 'Python', 10)
cool_mentor.rate_hw(best_student1, 'Python', 10)
print(best_student1)

lecturer1 = Lecturer('Prof','Prof_')
lecturer1.courses_attached += ['Python']
best_student.rate_lecturer('Python', lecturer1, 5)
best_student1.rate_lecturer('Python', lecturer1, 10)

lecturer2 = Lecturer('Prof','Prof_')
lecturer2.courses_attached += ['Python']
best_student.rate_lecturer('Python', lecturer2, 5)
best_student1.rate_lecturer('Python', lecturer2, 9)

print(lecturer1.eval_points)
print(cool_mentor)
print(lecturer1)
print(best_student)
print(best_student < best_student1)
print(lecturer2 < lecturer1)
print(best_student == best_student1)
print(lecturer2 == lecturer1)

def stud_aver_course(students, course):
    aver_sum = 0
    aver_count = 0
    for student in students:
        if not isinstance(student, Student):
            return
        if not course in student.grades:
            return
        course_grades = student.grades[course]
        aver_sum += sum(course_grades)
        aver_count += len(course_grades)
    return round(aver_sum / aver_count, 2)

def lect_aver_course(lectureres, course):
    aver_sum = 0
    aver_count = 0
    for lecturer in lectureres:
        if not isinstance(lecturer, Lecturer):
            return
        if not course in lecturer.eval_points:
            return
        lecturer_points = lecturer.eval_points[course]
        aver_sum += sum(lecturer_points)
        aver_count += len(lecturer_points)
    return round(aver_sum / aver_count, 2)

res1 = stud_aver_course([best_student, best_student1], 'Python')
res2 = lect_aver_course([lecturer1, lecturer2], 'Python')

print(res1)
print(res2)