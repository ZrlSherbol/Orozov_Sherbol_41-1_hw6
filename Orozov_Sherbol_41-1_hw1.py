class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"My name is {self.fullname}. I am {self.age} years old.")
        if self.is_married:
            print("I am married.")
        else:
            print("I am not married.")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def introduce_myself(self):
        super().introduce_myself()
        print("I am a student.")
        print("My marks are:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def average_mark(self):
        total_marks = sum(self.marks.values())
        average_mark = total_marks / len(self.marks)
        return average_mark

class Teacher(Person):
    base_salary = 5000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus_percentage = 0
        if self.experience > 3:
            bonus_percentage = (self.experience - 3) * 0.05
        total_salary = self.base_salary * (1 + bonus_percentage)
        return total_salary


teacher = Teacher("Alina Tolomushova", 45,
                  True, 8)


print("Teacher: ")
teacher.introduce_myself()
print(f"Experience: {teacher.experience} years")
print(f"Base Salary: ${teacher.base_salary}")
salary = teacher.calculate_salary()
print(f"Calculated Salary: ${salary}\n")


def create_students():
    students = []

    student1 = Student("Alisa Mekeshova",
                       15, False,
                       {"Math": 3, "Physics": 4, "Chemistry": 4})
    students.append(student1)

    student2 = Student("Bilal Orozov", 15, False,
                       {"Math": 5, "Physics": 5, "Chemistry": 4})
    students.append(student2)

    student3 = Student("Alihan Mamataliyev", 15, False,
                       {"Math": 3, "Physics": 4, "Chemistry": 3})
    students.append(student3)

    return students

students_list = create_students()
for i, student in enumerate(students_list, 1):
    print(f"\nStudent {i}:")
    student.introduce_myself()
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")

    average_mark = student.average_mark()
    print(f"Average Mark: {average_mark}")