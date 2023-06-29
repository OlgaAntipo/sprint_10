import data
import requests
import configuration


# 1. создание пользователя
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,  # тут тело
                         headers=data.headers)  # заголовки


# 2. изменение значения в параметре authToken
def qet_new_user_token():
    current_body = data.user_body
    resp_user = post_new_user(current_body)
    return resp_user.json()["authToken"]


# 3. создание набора
def post_new_kit(kit_body):
    headers_dict = data.headers.copy()
    auth_token = qet_new_user_token()
    headers_dict["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,  # тут тело
                         headers=headers_dict)  # заголовки
