family=[
    {
        "name":"Ashik",
        "age" : "18",
        "favourite color" : "blue"
    },
    {
        "name" :"Oboni",
        "age" : "12",
        "favourite color" : "pink"

    },
    {
        "name":"Maya",
        "age":"65",
        "favourite color":"White"
    },
    {
        "name":"Minu",
        "age":"38",
        "favourite color":"Orange"
    },
    {
        "name":"Riya",
        "age":"27",
        "favourite color":"Green"
    },
    {
        "name":"Bristy",
        "age":"30",
        "favourite color":"Yellow"
    },
    {
        "name":"Minhaz",
        "age":"75",
        "favourite color":"Red"
    },
    {
        "name": "Rifat",
        "age" : "31",
        "favourite color" : "White"

    },
    {
        "name" : "Shakil",
        "age" : "34",
        "favourite color" : "Nevy Blue"

    },
    {
        "name" : "Nahin",
        "age" : "3",
        "favourite color" : "red"
    }



]



def age_search():
    search_bar= input("Enter a family member name: ").capitalize()
    for member in range(len(family)):

        if family[member]["name"] == search_bar:
            print("The age of {} is {}".format(family[member]["name"],family[member]["age"]))



def color_search():
    search_bar = input("Enter a family member name: ").capitalize()
    for member in range(len(family)):

        if family[member]["name"]==search_bar:
            print("The favourite color of {} is {}".format(family[member]["name"],family[member]["favourite color"]))






def main_menu():

    user_input= input("press 'a' to know the age ,press 'f' to know the favourite color or press 'q to close the app' : ")
    while user_input != "q":
        if user_input == "a" :
            age_search()
        elif user_input == "f":
            color_search()

        else:
            print("Unknown Command..... Please try again with a correct command")
        user_input= input("press 'a' to know the age ,press 'f' to know the favourite color or press 'q to close the app' : ")

main_menu()

