class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_grade(self):
        sum_ = []
        for course, grade in self.grades.items():
            av_sum = sum(grade) / len(grade)
            sum_.append(av_sum)
        return sum(sum_) / len(sum_)

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.av_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {','.join(self.finished_courses)}
'''
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.av_grade() < other.av_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_grade(self):
        sum_ = []
        for course, grade in self.grades.items():
            av_sum = sum(grade) / len(grade)
            sum_.append(av_sum)
        return sum(sum_) / len(sum_)

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.av_grade()}
'''
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.av_grade() < other.av_grade()


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
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
'''
        return res


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['CC+']
best_student.finished_courses += ['Java']

other_student = Student('Sam', 'Smith', 'male')
other_student.courses_in_progress += ['Python']
other_student.finished_courses += ['Other_course']

cool_mentor = Mentor('Alise', 'Wonder')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['CC+']

cool_lecturer = Lecturer('James', 'Bond')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['CC+']

other_lecturer = Lecturer('Anna', 'Onim')
other_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Stive', 'King')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['CC+']

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'CC+', 10)

other_student.rate_hw(other_lecturer, 'Python', 10)
other_student.rate_hw(other_lecturer, 'Python', 9)
other_student.rate_hw(other_lecturer, 'Python', 8)
other_student.rate_hw(other_lecturer, 'CC+', 10)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'CC+', 10)

cool_reviewer.rate_hw(other_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 9)
cool_reviewer.rate_hw(other_student, 'Python', 8)


# print(cool_lecturer > other_lecturer)
# print(best_student > other_student)
# print(best_student)
# print(cool_lecturer)
# print(cool_reviewer)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# print(cool_lecturer.grades)
# print(best_student.grades)

def comp_stud_grades(some_stud_list, course):
    sum_ = 0
    count = 0
    for student in some_stud_list:
        if course in student.courses_in_progress:
            av_grade_of_course = sum(student.grades[course]) / len(student.grades[course])
            count += 1
            sum_ += av_grade_of_course
            return sum_ / count
        else:
            print('Студент не проходит данный курс')


def comp_lect_grades(some_lect_list, course):
    sum_ = 0
    count = 0
    for lecturer in some_lect_list:
        if course in lecturer.courses_attached:
            av_grade_of_course = sum(lecturer.grades[course]) / len(lecturer.grades[course])
            count += 1
            sum_ += av_grade_of_course
            return sum_ / count
        else:
            print('Лектор не преподает данный курс')


student_list = [best_student, other_student]
lecturer_list = [cool_lecturer, other_lecturer]

comp_stud_grades(student_list, 'Python')
# print(comp_stud_grades(student_list, 'CC+'))

comp_lect_grades(lecturer_list, 'Python')


# print(comp_lect_grades(lecturer_list, 'Python'))
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
