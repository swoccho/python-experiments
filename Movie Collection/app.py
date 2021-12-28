from utils import database

Users_choice = """
- press 'a' to add a new movie in your collection,
- press 'w' to mark a movie as watched ,
- press 'r' to remove a movie from your collection,
- press 'l' to see the list of your movie collection,
- press 'all' to remove all the movie from your collection,
- press 'c' to mark all movie as watched,
- press 'q' to quit . 
"""


def menu():
    database.create_file()
    user_input = input(Users_choice).lower()
    while user_input != "q":
        if user_input == "a":
            prompt_add_movie()
        elif user_input == 'w':
            prompt_mark_watched()
        elif user_input == "r":
            prompt_remove_movie()
        elif user_input == "l":
            show_movie()
        elif user_input == "all":
            remove_all()

        elif user_input == "c":
            watched_all()
        else:
            print("Unknown Command. Please try again.......")

        user_input = input(Users_choice).lower()


def prompt_add_movie():
    name = input("Enter the name of a movie: ").title()
    language = input("Enter the movie language: ").title()
    database.add_movie(name, language)


def prompt_mark_watched():
    name = input("Enter the movie name which you want to mark as watched: ").title()

    database.mark_as_watched(name)


def show_movie():
    movies = database.get_all_movie()

    for movie in movies:
        print(f"{movie['name']} is a {movie['language']} movie, {movie['status']} ")

    if not movies:
        print("You have not added any movie in your collection yet... Please add some movie in your collection.")


def prompt_remove_movie():
    name = input("Enter the movie name which you want to remove from your collection: ").title()

    database.remove_movie(name)


def remove_all():
    database.remove()


def watched_all():
    database.all_watched()


menu()
