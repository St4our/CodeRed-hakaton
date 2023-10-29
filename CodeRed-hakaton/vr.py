import time
import requests

# ----------------------для кнопки забыл пароль--------------------------#


def recovery_send_code(email): # есди успешно - отправляет код на почту
    url = 'https://0435-176-28-64-201.ngrok-free.app/api/recovery'
    headers = {"Content-Type": "application/json",
               "ngrok-skip-browser-warning": "69420"}
    data = {"email": email}

    r = requests.post(url=url, json=data, headers=headers)
    if r.status_code == 200:
        return 'recovery mail sended'


def recovery_code_check(email, recovery_code):  # проверяет правильный ли код я хз надо ли это
    url = 'https://0435-176-28-64-201.ngrok-free.app/api/confirmation'
    headers = {"Content-Type": "application/json",
               "ngrok-skip-browser-warning": "69420"}
    data = {"email": email,
            "recoveryCode": recovery_code}

    r = requests.post(url=url, json=data, headers=headers)
    if r.status_code == 200:
        return 'recovery code is real'
    else:
        return 'wrong recovery code!'


def recovery_code_pull(email, password, recovery_code):  # меняет пароль на указанный - возвращает токены и роль
    url = 'https://0435-176-28-64-201.ngrok-free.app/api/reset'
    headers = {"Content-Type": "application/json",
               "ngrok-skip-browser-warning": "69420"}
    data = {"email": email,
            "password": password,
            "recoveryCode": recovery_code}

    r = requests.post(url=url, json=data, headers=headers)
    if r.status_code == 200:
        info = r.json()
        access_token = info['tokenPair']['accessToken']
        refresh_token = info['tokenPair']['refreshToken']
        role = info['role']
        return access_token, refresh_token, role
    else:
        return 'wrong recovery code!'


def recovery():
    email = input('enter mail: ')
    print(recovery_send_code(email))  # отправляет пиьсмо на почту

    # code = input()
    # print(recovery_code_check(email, code))  # проверяет правильный ли код я хз надо ли это проверять
    code = input('enter code: ')
    passw = input('enter new password: ')
    print(recovery_code_pull(email, passw, code))  # меняет пароль на указанный но если
# ----------------------для кнопки забыл пароль--------------------------#


def authtorization(user_mail, user_pass):  # авторизация ползователя - возвращает токены и роль
    url = 'https://0435-176-28-64-201.ngrok-free.app/api/signin'
    headers = {"Content-Type": "application/json",
               "ngrok-skip-browser-warning": "69420"}

    data = {"email": user_mail,
            "password": user_pass}

    r = requests.post(url=url, json=data, headers=headers)
    if r.status_code == 200:
        info = r.json()
        access_token = info['tokenPair']['accessToken']
        refresh_token = info['tokenPair']['refreshToken']
        role = info['role']
        return access_token, refresh_token, role
    else:
        return 'failed'


def registration(user_mail, user_pass):  # регистрация ползователя - возвращает токены и роль
    url = 'https://0435-176-28-64-201.ngrok-free.app/api/signup'
    headers = {"Content-Type": "application/json",
               "ngrok-skip-browser-warning": "69420"}

    data = {"email": user_mail,
            "password": user_pass}

    r = requests.post(url=url, json=data, headers=headers)
    if r.status_code == 200:
        info = r.json()
        access_token = info['tokenPair']['accessToken']
        refresh_token = info['tokenPair']['refreshToken']
        role = info['role']
        return access_token, refresh_token, role
    else:
        return 'failed'


def get_all_sessions(access_token, moduleName):  # получение всех доступных сессий
    url = f'https://0435-176-28-64-201.ngrok-free.app/api/sessions/{moduleName}'
    headers = {"Content-Type": "application/json",
               "ngrok-skip-browser-warning": "69420",
               "Authorization": access_token}

    r = requests.get(url=url, headers=headers)
    info = r.json()
    return info


def auth():
    login = input()
    password = input()
    stat = authtorization(login, password)
    if stat == 'failed':
        print('wrong mail or password')
    else:
        access_token, refresh_token, role = authtorization(login, password)
        print('вошёл')
        while True:
            info = get_all_sessions(access_token, 'Сварщики')
            print(info)
            if len(info) > 0:
                score = info[0]["score"]
                print('score: ', score)
                break
            print('пока ждём')
            time.sleep(10)

# reg = registration(login, password)
#
# if reg == 'failed':
#     access_token, refresh_token, role = authtorization(login, password)
# else:
#     access_token, refresh_token, role = reg
# print('вошёл')
