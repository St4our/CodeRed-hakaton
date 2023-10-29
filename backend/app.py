from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from funcs import *
import sqlite3
import os.path
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
connection = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = connection.cursor()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
version = "v1"

@app.route(f'/{version}/hello', methods=['POST'])
def hello_post():
    try:
        data = request.get_json()
        result = {}
        fio = data['params']['fio']
        number = data['params']['number']
        inn = data['params']['inn']
        mail = data['params']['mail']
        organization = data['params']['organization']
        adress = data['params']['adress']
        cont = f"""
            ФИО : {fio}\n

            Номер телефона: {number}\n

            ИНН организации: {inn}\n

            Почта: {mail}\n

            Организация: {organization}\n

            Адрес организации: {adress}\n

            """
        f_host = "smtp.beget.com"
        f_port = "2525"
        f_user = "codered_it@coderedit.ru"
        f_passwd = "Stas_2001"
        to = "okolofutbol07@gmail.com"
        smtpserver = smtplib.SMTP(f_host, f_port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(f_user, f_passwd)  # from email credential
        msg = MIMEText(cont, 'html')
        msg['From'] = "codered_it@coderedit.ru"
        msg['To'] = to
        smtpserver.sendmail(f_user, to, msg.as_string())
        smtpserver.close()
        print('Mail is sent successfully!!')
        result["success"] = True
    except Exception as exception:
        result["success"] = False; result["error_msg"] = str(exception)
    return jsonify(result)

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
            data = request.get_json()
            name = data['params']['name']
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
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/login", methods=["POST"])
def login_post() -> json:
    data = request.get_json()
    result = {}
    username = data['params']['username']
    password = data['params']['password']
    token = make_token(username, password)
    print(username, password, token)
    try:
        if is_token_valid(cursor, token): 
            result["success"] = True
            cursor.execute(f"select user_id from users where token = '{token}'")
            user_id = cursor.fetchone()[0]
            users_data = get_users(connection, cursor, user_id)
            result["success"] = True; result["users"] = users_data
        else: result["success"] = False; result["error_msg"] = "Authorization data is not valid"
    except Exception as exception:
        result["success"] = False; result["error_msg"] = str(exception)
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
    print(token, request.headers)
    if is_token_valid(cursor, token):
        try:
            data = request.get_json()
            sec_role = data['params']['sec_role']
            organization_id = data['params']['organization_id']
            category_id = data['params']['category_id']
            username = data['params']['username']
            password = data['params']['password']
            name = data['params']['name']
            surname = data['params']['surname']
            phone = data['params']['phone']
            email = data['params']['email']
            token = make_token(username, password)
            user_id = create_user(connection, cursor, sec_role, organization_id, category_id, username, token, name, surname, phone, email)
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
            result["success"] = False; result["error_msg"] = str(exception)
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
            data = request.get_json()
            name = data['params']['name']
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
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/lessons", methods=["GET"])
def lessons_get() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            lesson_id = request.args.get('lesson_id')
            lessons_data = get_lessons(connection, cursor, lesson_id)
            result["success"] = True; result["lessons"] = lessons_data
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/lessons", methods=["POST"])
def lessons_post() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            data = request.get_json()
            video_src = data['params']['video_src']
            title = data['params']['title']
            lesson_id = create_lesson(connection, cursor, video_src, title)
            result["success"] = True; result["lesson_id"] = lesson_id
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/lessons", methods=["DELETE"])
def lessons_delete() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            lesson_id = request.args.get('lesson_id')
            delete_lesson(connection, cursor, lesson_id)
            result["success"] = True
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/tests", methods=["GET"])
def tests_get() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            test_id = request.args.get('test_id')
            tests_data = get_tests(connection, cursor, test_id)
            result["success"] = True; result["tests"] = tests_data
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

@app.route(f"/{version}/tests", methods=["POST"])
def tests_post() -> json:
    token = request.headers.get('Authorization'); result = {}
    if is_token_valid(cursor, token):
        try:
            result["questions_id"] = []
            data = request.get_json()
            name = data['params']['name']
            questions = data['params']['questions']
            test_id = create_test(connection, cursor, name)
            for question in questions:
                question_id = create_question(connection, cursor, test_id, question["name"], question["answer_1"], question["answer_2"], question["answer_3"], question["correct_id"])
                result["questions_id"].append(question_id)
            result["success"] = True; result["test_id"] = test_id
        except Exception as exception:
            result["success"] = False; result["error_msg"] = str(exception)
    else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
    return jsonify(result)

# @app.route(f"/{version}/tests", methods=["DELETE"])
# def tests_delete() -> json:
#     token = request.headers.get('Authorization'); result = {}
#     if is_token_valid(cursor, token):
#         try:
#             test_id = request.args.get('test_id')
#             delete_test(connection, cursor, test_id)
#             result["success"] = True
#         except Exception as exception:
#             result["success"] = False; result["error_msg"] = exception
#     else: result["success"] = False; result["error_msg"] = "Authorization token is not valid"
#     return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=False)