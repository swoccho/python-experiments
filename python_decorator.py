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