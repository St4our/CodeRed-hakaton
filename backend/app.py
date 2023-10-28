from funcs import make_token, is_token_valid, get_users, create_user, delete_user, get_categories, create_category, delete_category, get_organizations, create_organization, delete_organization
from flask import Flask, request, jsonify
import sqlite3
import os.path
import json

def sql_scheme(cursor: sqlite3.Cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS organizations (organization_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY NOT NULL, organization_id INTEGER NOT NULL, sec_role_id INTEGER NOT NULL, category_id INTEGER, username TEXT NOT NULL, token TEXT NOT NULL, date_of_birth TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS categories (category_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS sec_roles (sec_role_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL)""")

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
connection = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = connection.cursor(); sql_scheme(cursor)
app = Flask(__name__)
version = "v1"

@app.route(f"/{version}/organizations", methods=["GET"])
def organizations_get() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            organization_id = request.args.get('organization_id')
            organizations_data = get_organizations(connection, cursor, organization_id)
            result["success"] = True; result["organizations"] = organizations_data
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/organizations", methods=["POST"])
def organizations_post() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            name = request.args.get('name')
            organization_id = create_organization(connection, cursor, name)
            result["success"] = True; result["organization_id"] = organization_id
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/organizations", methods=["DELETE"])
def organizations_delete() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            organization_id = request.args.get('organization_id')
            delete_organization(connection, cursor, organization_id)
            result["success"] = True
        except Exception as exception:
            result["success"] = False; result["error_msg"] = exception
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/users", methods=["GET"])
def users_get() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            user_id = request.args.get('user_id')
            users_data = get_users(connection, cursor, user_id)
            result["success"] = True; result["users"] = users_data
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/users", methods=["POST"])
def users_post() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            sec_role_id = request.args.get('sec_role_id')
            category_id = request.args.get('category_id')
            username = request.args.get('username')
            password = request.args.get('password')
            date_of_birth = request.args.get('date_of_birth')
            token = make_token(username, password)
            user_id = create_user(connection, cursor, sec_role_id, category_id, username, token, date_of_birth)
            result["success"] = True; result["user_id"] = user_id
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/users", methods=["DELETE"])
def users_delete() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            user_id = request.args.get('user_id')
            delete_user(connection, cursor, user_id)
            result["success"] = True
        except Exception as exception:
            result["success"] = False; result["error_msg"] = exception
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/categories", methods=["GET"])
def categories_get() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            category_id = request.args.get('category_id')
            categories_data = get_categories(connection, cursor, category_id)
            result["success"] = True; result["categories"] = categories_data
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/categories", methods=["POST"])
def categories_post() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            name = request.args.get('name')
            category_id = create_category(connection, cursor, name)
            result["success"] = True; result["category_id"] = category_id
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/categories", methods=["DELETE"])
def categories_delete() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            category_id = request.args.get('category_id')
            delete_category(connection, cursor, category_id)
            result["success"] = True
        except Exception as exception:
            result["success"] = False; result["error_msg"] = exception
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)