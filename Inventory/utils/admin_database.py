import sqlite3
import smtplib
from email.message import EmailMessage

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

#
# def admin_pass_recovery(email,otp):
#
#     email_ =EmailMessage()
#     email_["Subject"] = "Password Recovery"
#     email_["From"] = gmail,
#     email_["To"] = email
#
#     email_.set_content(f"Your password recovery OTP is {otp}")
#
#
#     smtp_connection = smtplib.SMTP("smtp.gmail.com",port=587)
#     smtp_connection.starttls()
#     smtp_connection.login(gmail,password)
#     smtp_connection.send_message(email_)
#     smtp_connection.quit()
#     print("OTP sent to your E-mail..... Please check your E-mail")
#
#
# def recovery_pass_update(new_pass,username):
#     connection = sqlite3.connect("admin.db")
#     cursor= connection.cursor()
#     cursor.execute("UPDATE accounts SET password =? WHERE username =?",(new_pass,username,))
#     connection.commit()
#     connection.close()

