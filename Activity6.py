class Student:
    def __init__(self, grade):
        self.__grade = grade

    def study(self):
        print("Student is studying.")

class CollegeStudent(Student):
    def study(self):
        print("College student is studying programming.")

s = Student(10)
cs = CollegeStudent(12)

s.study()
cs.study()