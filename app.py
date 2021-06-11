
movies = []
def add_movie():
         title = input("Enter a movie title : ")
         director = input("Enter the director name : ")
         year = input("Enter the launching year of the movie : ")
         movies.append(
                {
                        "title" : title,
                        "director": director,
                        "launching year" : year
                })
def show_movie():
        for movie in movies:
                print_movie(movie)


def print_movie(movie):
        print(f"title : {movie['title']}")
        print(f"director: {movie['director']}")
        print(f"released year: {movie['launching year']}")


def search_movie():
        user_input = input("Enter the movie name what are you looking for : ")
        for movie in movies:
                if movie["title"] == user_input:
                        print_movie(movie)



def menu():
        asking = input("Enter 'add' to add, Enter 'see' to see movie list ,Enter 'search' to search movie from your collection or Enter 'exit' to close the app :  ").lower()
        while asking != "q":
                if asking == "add":
                        add_movie()
                elif asking == "see":
                        show_movie()
                elif asking == "search":
                        search_movie()
                else:
                        print("Error.... Please try again with a valid keyword")

                asking = input("Enter 'add' to add, Enter 'see' to see movie list ,Enter 'search' to search movie from your collection or Enter 'exit' to close the app :  ").lower()
menu()



