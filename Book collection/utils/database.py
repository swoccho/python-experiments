import json

books_file = "books.json"

def create_book_file():
    with open(books_file,"w") as file :
        json.dump([], file)





def add_books(name,author):
    books = get_all_books()
    books.append(
        {
            "name" : name,
            "author": author,
            "read": "Not read"
        }
    )
    _save_all_books(books)





def get_all_books():
    with open(books_file,"r")as file:
        return json.load(file)



def mark_as_read(name):
    books = get_all_books()

    for book in books:
        if book["name"] == name:
            book["read"] = "Completed"

    _save_all_books(books)


def _save_all_books(books):
    with open(books_file,"w")as file:
        json.dump(books,file,indent=6)



def remove_book(name):
    books = get_all_books()
    books = [book for book in books if book["name"] != name]
    _save_all_books(books)