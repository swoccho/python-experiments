import sqlite3


def admin_create_table():
    connection = sqlite3.connect("admin.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (username text primary key, password text , Email text)")
    connection.commit()
    connection.close()


def add_admin_data(username, password, email):
    connection = sqlite3.connect("admin.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts VALUES(?,?,?)", (username, password, email,))
    connection.commit()
    connection.close()


def admin_data():
    connection = sqlite3.connect("admin.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts")
    all_data = [{"username": row[0], "password": row[1], "email": row[2]} for row in cursor.fetchall()]

    return all_data


def default_user():
    return "admin"



