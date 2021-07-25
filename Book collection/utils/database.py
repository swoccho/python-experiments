import sqlite3



def create_book_file():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key , author text , read text)')
    connection.commit()
    connection.close()


def add_books(name,author):
    connection = sqlite3.connect("data.db")
    cursor =connection.cursor()
    try:
        cursor.execute('INSERT INTO books VALUES(?,?,?)',(name, author,"not read"))
    except sqlite3.IntegrityError:
        print("you already have a book of that name")
    connection.commit()
    connection.close()



def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{"name":row[0] , "author": row[1] , "read": row[2] } for row in cursor.fetchall()]

    connection.close()
    return books


def mark_as_read(name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read="Completed" WHERE name= ?' , (name,))
    connection.commit()
    connection.close()


def remove_book(name):

    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books  WHERE name= ?' , (name,))
    connection.commit()
    connection.close()
