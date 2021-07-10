from utils import database




USER_CHOICE ="""
Enter:
- press 'a' to add books,
- press 'del' to remove books,
- press 's' to see the book list,
- press 'r' to mark a book as read,
- press 'q' to quit.

Your Choice: """

def menu():
    database.create_book_file()
    user_prompt = input(USER_CHOICE)
    while user_prompt != "q":
        if user_prompt == "a":
            prompt_add_books()

        elif user_prompt == "del":
            prompt_remove_book()
        elif user_prompt == "s":
            show_books()

        elif user_prompt== "r":
            prompt_mark_as_read()
        else:
            print("Unknown command.... Please try again...")

        again = input(
                      "Want to Interact Again ?? (Y/n): ").lower()
        if again == "y":
            user_prompt = input(USER_CHOICE)
        else:
            return





def prompt_add_books():
    name = input("Enter a book name: ").title()
    author = input("Enter the book Author name: ").title()
    database.add_books(name,author)


def show_books():
    books = database.get_all_books()
    for book in books:
        print(f"{book['name']} by {book['author']} ,{book['read']} \n")



def prompt_mark_as_read():
    name = input("Enter the name of the book which you want to mark as read: ").title()

    database.mark_as_read(name)


def prompt_remove_book():
    name = input("Enter the name which you want to remove from your collection: ").title()
    database.remove_book(name)




menu()