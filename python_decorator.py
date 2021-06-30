class Student:
    def __init__(self, name,school):
        self.name = name
        self.school = school
        self. marks =[]
    @property
    def average(self):
        return sum(self.marks)/ len(self.marks)
student_1 =Student("Rafid", "V.J")
student_1.marks.append(54)
student_1.marks.append(55)
student_1.marks.append(98)
student_1.marks.append(98)
print(student_1.average)

class Workingstudent(Student):
    def __init__(self,name,school, salary):
        super().__init__(name,school)
        self.salary = salary
    @property
    def monthly_salary(self):
        return self.salary * 30
worker_1 = Workingstudent("shakib","cumilla high school", 100)
print(worker_1.monthly_salary)

class Greet:
    def hello(cls):
        return


