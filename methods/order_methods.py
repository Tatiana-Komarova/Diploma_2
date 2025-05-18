import requests
from data import Url
import allure

class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(token: str, ingredients: list):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}', headers={"Authorization": token}, json={"ingredients": ingredients})

    @staticmethod
    @allure.step('Получение списка заказов конкретного пользователя')
    def get_user_orders(token: str):
        return requests.get(f'{Url.BASE_URL}{Url.GET_USER_ORDER_URL}', headers={"Authorization": token})

