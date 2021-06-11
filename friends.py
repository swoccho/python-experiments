# user_input = input("Enter Your friend Name: \n")
# friends = ["Rafid","Asif", "Tahmid", "Shaon", "Jim", "Tanim"]
# if user_input.capitalize() in friends:
#     print(f"{user_input.title()} is one of your friends")
# else:
#     print(f"{user_input.title()} is not your friend")


friends = ["Rafid","Asif", "Tahmid", "Shaon", "Jim", "Tanim"]
guests = ["Rakib", "Nilloy" , "Suvo" , "Shakib" , "Ratul" , " Rafid" , "Tanim", "Shaon"]
present_friends = [
    friend.title() for friend in guests if friend.capitalize() in friends
]
print(present_friends)




