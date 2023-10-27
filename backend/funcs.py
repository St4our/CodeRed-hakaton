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
    cursor.execute(f"INSERT INTO organizations(organization_id, name) VALUES ((SELECT ifnull(max(organization_id), 0)+1 from organizations), '{name}')"); connection.commit()
    organization_id = cursor.lastrowid
    return organization_id

def delete_organization(connection: sqlite3.Connection, cursor: sqlite3.Cursor, organization_id: int) -> None:
    cursor.execute(f"DELETE FROM organizations where organization_id = {organization_id}"); connection.commit()

def get_users(connection: sqlite3.Connection, cursor: sqlite3.Cursor, user_id: int) -> json:
    cols = ["user_id", "sec_role_id", "category_id", "username", "date_of_birth"]
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

def create_user(connection: sqlite3.Connection, cursor: sqlite3.Cursor, sec_role_id: int, category_id: int, username: str, token: str, date_of_birth: str) -> json:
    cursor.execute(
        "INSERT INTO users(user_id, sec_role_id, category_id, username, token, date_of_birth) VALUES "
        "((SELECT max(ifnull(user_id, 0))+1 from users), ?, ?, ?, ?, ?)",
        (sec_role_id, category_id, username, token, date_of_birth)
    ); connection.commit()
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
    cursor.execute(f"INSERT INTO categories(category_id, name) VALUES ((SELECT ifnull(max(category_id), 0)+1 from categories), '{name}')"); connection.commit()
    category_id = cursor.lastrowid
    return category_id

def delete_category(connection: sqlite3.Connection, cursor: sqlite3.Cursor, category_id: int) -> None:
    cursor.execute(f"DELETE FROM categories where category_id = {category_id}"); connection.commit()