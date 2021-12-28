from .database_connection import DatabaseConnection


def create_file():
    with DatabaseConnection("movie.db") as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS movies(name text primary key , language text , status text)')


def add_movie(name, language):
    with DatabaseConnection('movie.db') as connection:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO movies VALUES(?,?,?)", (name, language, "not watched"))


def mark_as_watched(name):
    with DatabaseConnection("movie.db") as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE movies SET status='watched' WHERE name= ?", (name,))


def get_all_movie():
    with DatabaseConnection("movie.db") as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM movies")

        movies = [{"name": row[0], "language": row[1], "status": row[2]} for row in cursor.fetchall()]

        return movies


def remove_movie(name):
    with DatabaseConnection("movie.db") as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM movies WHERE name=?", (name,))


def remove():
    with DatabaseConnection("movie.db") as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM movies ")


def all_watched():
    with DatabaseConnection("movie.db") as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE movies SET status='watched'")
