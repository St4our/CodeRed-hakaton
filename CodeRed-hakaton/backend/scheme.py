from funcs import *
import sqlite3

connection = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS organizations (organization_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY NOT NULL, organization_id INTEGER NOT NULL, sec_role TEXT NOT NULL, category_id INTEGER NOT NULL, username TEXT NOT NULL, token TEXT NOT NULL, name TEXT NOT NULL, surname NOT NULL, phone TEXT NOT NULL, email TEXT NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS categories (category_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS lessons (lesson_id INTEGER PRIMARY KEY NOT NULL, video_src TEXT NOT NULL, title TEXT NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS tests (test_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS questions (question_id INTEGER PRIMARY KEY NOT NULL, test_id INTEGER NOT NULL, name TEXT NOT NULL, answer_1 TEXT NOT NULL, answer_2 TEXT NOT NULL, answer_3 TEXT NOT NULL, correct_id INTEGER NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS user_answers (user_answers_id INTEGER PRIMARY KEY NOT NULL, user_id INTEGER NOT NULL, question_id INTEGER NOT NULL, answer_id INTEGER NOT NULL)""")

admin_token = make_token("admin", "admin")
admin_id = create_user(connection, cursor, 'super', 0, 0, 'admin', admin_token, 'admin_name', 'admin_surname', '+123-45-67', 'admin@fake_mail.com')
print("Admin id:", admin_id, "- Admin token:", admin_token)