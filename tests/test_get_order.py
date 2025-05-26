import pytest
import allure
from methods.order_methods import OrderMethods

class TestGetOrder:
    @allure.title('Получить список заказов авторизованного ползователя')
    @allure.step('Проверка кода и ответа')
    def test_get_orders_authorized(self, auth_token):
        response = OrderMethods.get_user_orders(auth_token)
        assert response.status_code == 200
        js = response.json()
        assert js.get("success") is True
        assert isinstance(js.get("orders"), list)

    @allure.title('Получить список заказов неавторизованного пользователя')
    @allure.step('Проверка кода и ответа')
    def test_get_orders_unauthorized(self):
        response = OrderMethods.get_user_orders(token="")
        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"

