import sqlite3
import base64
import json

def make_token(username: str, password: str):
    auth_string = f"{username}:{password}"
    token = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
    return token

def is_token_valid(cursor: sqlite3.Cursor, token: str):
    try:
        username, password = base64.b64decode(token).decode('utf-8').split(":")
        cursor.execute(f"""SELECT token FROM users WHERE username = '{username}' and token = '{token}'""")
        token = cursor.fetchone()
        if token: return True
    except: pass
    return False

def get_organizations(connection: sqlite3.Connection, cursor: sqlite3.Cursor, organization_id: int) -> json:
    cols = ["organization_id", "name"]
    if organization_id: cursor.execute(f"SELECT {','.join(col for col in cols)} from organizations WHERE organization_id = {organization_id}")
    else: cursor.execute(f"SELECT {','.join(col for col in cols)} from organizations")
    users = cursor.fetchall()
    users_data = []
    for user in users:
        user_info = {}
        for col_cnt, col in enumerate(cols):
            user_info[col] = user[col_cnt]
        users_data.append(user_info)
    return users_data

def create_organization(connection: sqlite3.Connection, cursor: sqlite3.Cursor, name: str) -> json:
    cursor.execute(f"INSERT INTO organizations(organization_id, name) VALUES ((SELECT ifnull(max(organization_id), 0)+1 from organizations), '{name}')")
    connection.commit()
    organization_id = cursor.lastrowid
    return organization_id

def delete_organization(connection: sqlite3.Connection, cursor: sqlite3.Cursor, organization_id: int) -> None:
    cursor.execute(f"DELETE FROM organizations where organization_id = {organization_id}"); connection.commit()

def get_users(connection: sqlite3.Connection, cursor: sqlite3.Cursor, user_id: int) -> json:
    cols = ["user_id", "organization_id", "sec_role", "category_id", "username", "token", "name", "surname", "phone", "email"]
    if user_id: cursor.execute(f"SELECT {','.join(col for col in cols)} from users WHERE user_id = {user_id}")
    else: cursor.execute(f"SELECT {','.join(col for col in cols)} from users")
    users = cursor.fetchall()
    users_data = []
    for user in users:
        user_info = {}
        for col_cnt, col in enumerate(cols):
            user_info[col] = user[col_cnt]
        users_data.append(user_info)
    return users_data

def create_user(connection: sqlite3.Connection, cursor: sqlite3.Cursor, sec_role: int, organization_id: int, category_id: int, username: str, token: str, name: str, surname: str, phone: str, email: str) -> json:
    cols = ["user_id", "organization_id", "sec_role", "category_id", "username", "token", "name", "surname", "phone", "email"]
    cursor.execute(
        f"INSERT INTO users({','.join(col for col in cols)}) VALUES "
        "((SELECT max(ifnull(user_id, 0))+1 from users), ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (organization_id, sec_role, category_id, username, token, name, surname, phone, email)
    )
    connection.commit()
    user_id = cursor.lastrowid
    return user_id

def delete_user(connection: sqlite3.Connection, cursor: sqlite3.Cursor, user_id: int) -> None:
    cursor.execute(f"DELETE FROM users where user_id = {user_id}",); connection.commit()

def get_categories(connection: sqlite3.Connection, cursor: sqlite3.Cursor, category_id: int) -> json:
    cols = ["category_id", "name"]
    if category_id: cursor.execute(f"SELECT {','.join(col for col in cols)} from categories WHERE category_id = {category_id}")
    else: cursor.execute(f"SELECT {','.join(col for col in cols)} from categories")
    users = cursor.fetchall()
    users_data = []
    for user in users:
        user_info = {}
        for col_cnt, col in enumerate(cols):
            user_info[col] = user[col_cnt]
        users_data.append(user_info)
    return users_data

def create_category(connection: sqlite3.Connection, cursor: sqlite3.Cursor, name: str) -> json:
    cursor.execute(f"INSERT INTO categories(category_id, name) VALUES ((SELECT ifnull(max(category_id), 0)+1 from categories), '{name}')")
    connection.commit()
    category_id = cursor.lastrowid
    return category_id

def delete_category(connection: sqlite3.Connection, cursor: sqlite3.Cursor, category_id: int) -> None:
    cursor.execute(f"DELETE FROM categories where category_id = {category_id}"); connection.commit()

def get_lessons(connection: sqlite3.Connection, cursor: sqlite3.Cursor, lesson_id: int) -> json:
    cols = ["lesson_id", "video_src", "title"]
    if lesson_id: cursor.execute(f"SELECT {','.join(col for col in cols)} from lessons WHERE lesson_id = {lesson_id}")
    else: cursor.execute(f"SELECT {','.join(col for col in cols)} from lessons")
    users = cursor.fetchall()
    users_data = []
    for user in users:
        user_info = {}
        for col_cnt, col in enumerate(cols):
            user_info[col] = user[col_cnt]
        users_data.append(user_info)
    return users_data

def create_lesson(connection: sqlite3.Connection, cursor: sqlite3.Cursor, video_src: str, title: str) -> json:
    cursor.execute(f"INSERT INTO lessons(lesson_id, video_src, title) VALUES ((SELECT ifnull(max(lesson_id), 0)+1 from lessons), '{video_src}', '{title}')")
    connection.commit()
    lesson_id = cursor.lastrowid
    return lesson_id

def delete_lesson(connection: sqlite3.Connection, cursor: sqlite3.Cursor, lesson_id: int) -> None:
    cursor.execute(f"DELETE FROM lessons where lesson_id = {lesson_id}"); connection.commit()

def get_tests(connection: sqlite3.Connection, cursor: sqlite3.Cursor, test_id: int) -> json:
    if test_id: cursor.execute(f"SELECT test_id, name from tests WHERE test_id = {test_id}")
    else: cursor.execute(f"SELECT test_id, name from tests")
    tests = cursor.fetchall()
    tests_data = []
    for test in tests:
        print(test)
        cursor.execute(f"SELECT name, answer_1, answer_2, answer_3, correct_id FROM questions WHERE test_id = {test[0]}")
        questions = cursor.fetchall()
        test_data = {
            "test_id": test[0], "name": test[1], "questions": []
        }
        for question in questions:
            question_data = {
                "name": question[0],
                "answer_1": question[1],
                "answer_2": question[2],
                "answer_3": question[3],
                "correct_id": question[4]
            }
            test_data["questions"].append(question_data)
        tests_data.append(test_data)
    return tests_data

def create_test(connection: sqlite3.Connection, cursor: sqlite3.Cursor, name: str) -> json:
    cursor.execute(f"INSERT INTO tests(test_id, name) VALUES ((SELECT ifnull(max(test_id), 0)+1 from tests),'{name}')") 
    connection.commit()
    test_id = cursor.lastrowid
    return test_id

def delete_test(connection: sqlite3.Connection, cursor: sqlite3.Cursor, test_id: int) -> None:
    cursor.execute(f"DELETE FROM tests where test_id = {test_id}"); connection.commit()

# def get_questions(connection: sqlite3.Connection, cursor: sqlite3.Cursor, question_id: int) -> json:
#     cols = ["question_id", "text"]
#     if question_id: cursor.execute(f"SELECT {','.join(col for col in cols)} from questions WHERE question_id = {question_id}")
#     else: cursor.execute(f"SELECT {','.join(col for col in cols)} from questions")
#     users = cursor.fetchall()
#     users_data = []
#     for user in users:
#         user_info = {}
#         for col_cnt, col in enumerate(cols):
#             user_info[col] = user[col_cnt]
#         users_data.append(user_info)
#     return users_data

def create_question(connection: sqlite3.Connection, cursor: sqlite3.Cursor, test_id: int, name: str, answer_1: str, answer_2: str, answer_3: str, correct_id: int) -> json:
    cursor.execute(f"INSERT INTO questions(question_id, test_id, name, answer_1, answer_2, answer_3, correct_id) VALUES ((SELECT ifnull(max(question_id), 0)+1 from questions), {test_id}, '{name}', '{answer_1}', '{answer_2}', '{answer_3}', {correct_id})") 
    connection.commit()
    question_id = cursor.lastrowid
    return question_id

# def delete_question(connection: sqlite3.Connection, cursor: sqlite3.Cursor, question_id: int) -> None:
#     cursor.execute(f"DELETE FROM questions where question_id = {question_id}"); connection.commit()