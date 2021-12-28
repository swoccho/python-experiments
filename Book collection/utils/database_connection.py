import sqlite3


class DatabaseConnection:
    def __init__(self, file):
        self.connection = None
        self.file = file

    def __enter__(self):
        self.connection = sqlite3.connect(self.file)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()

        self.connection.close()
