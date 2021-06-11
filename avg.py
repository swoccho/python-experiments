#
# students = {
#     "name" : "rafid",
#     "grades" : [100,52,98,74,96]
# }
#
# def average_grade(student):
#     return sum(student["grades"]) / len(student["grades"])


class Friend:
    def __init__(self,new_name, new_grades):
        self.name =new_name
        self.grades = new_grades
    def average(self):
        return sum(self.grades) / len(self.grades)

friend_one = Friend("Rafid", [54,46,89,100,100,99])
friend_two =Friend("Tahmid", [78,98,99,89,96,100])

print(f"The average of {friend_one.name} is {friend_one.average()}")
print(f"The average of {friend_two.name} is {friend_two.average()}")