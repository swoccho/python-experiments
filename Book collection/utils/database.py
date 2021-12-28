import sqlite3

from .database_connection import DatabaseConnection


def create_book_file():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key , author text , read text)')


def add_books(name, author):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES(?,?,?)', (name, author, "not read"))
        except sqlite3.IntegrityError:
            print("you already have a book of that name")


def get_all_books():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]

        return books


def mark_as_read(name):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read="Completed" WHERE name= ?', (name,))


def remove_book(name):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books  WHERE name= ?', (name,))


def remove():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM books")
