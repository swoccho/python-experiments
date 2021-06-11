operations = {
    "average" : lambda seq : sum(seq) / len(seq),
    "total" : sum,
    "top" : max,
    "last": min
}
students = [
    {"name" :"Ashik" ,"Grades": (98,90,80,87,100)},
    {"name":"Rafid", "Grades" :(89,78,100, 100,99)},
    {"name":"Tahmid" ,"Grades":(78,65,90,100,87)},
    {"name":"Asif" , "Grades" :(98,78,58,78,99)},
    {"name":"Shaon" , "Grades":(78,98,99,100,52)}

]

for student in students:
    name = student["name"]
    grade = student["Grades"]
    print(f"student : {name}")
    user_input =  input("Enter 'average','total','top' or 'last' : ")

    operation = operations[user_input]
    print(operation(grade))