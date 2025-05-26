import requests
from data import Url
import allure

class UserMethods:
    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(body):
        return requests.post(Url.CREATE_USER_URL, json = body)

    @staticmethod
    @allure.step('Получить информацию о пользователе')
    def get_user_info(token: str):
        return requests.get(Url.GET_UPDATE_USER_URL, headers={"Authorization": token})

    @staticmethod
    @allure.step('Обноваить информацию о пользователе')
    def update_user_info(token: str, body: dict):
        return requests.patch(Url.GET_UPDATE_USER_URL, headers={"Authorization": token}, json=body)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(email: str, password: str):
        return requests.post(Url.LOGIN_USER_URL, json = {"email": email, "password": password})


