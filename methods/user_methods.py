import requests
from data import Url
import allure

class UserMethods:
    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_USER_URL}', json = body)

    @staticmethod
    @allure.step('Получить информацию о пользователе')
    def get_user_info(token: str):
        return requests.get(f'{Url.BASE_URL}{Url.GET_UPDATE_USER_URL}', headers={"Authorization": token})

    @staticmethod
    @allure.step('Обноваить информацию о пользователе')
    def update_user_info(token: str, body: dict):
        return requests.patch(f'{Url.BASE_URL}{Url.GET_UPDATE_USER_URL}', headers={"Authorization": token}, json=body)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(email: str, password: str):
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER_URL}', json = {"email": email, "password": password})


