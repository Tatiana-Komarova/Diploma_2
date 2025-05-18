import pytest
import allure
from methods.order_methods import OrderMethods

class TestOrderCreation:
    @allure.step('Создание заказа авторизованным пользователем')
    @allure.description('Проверка кода и ответа')
    def test_create_order_authorized(self, auth_token, ingredient_ids):
        response = OrderMethods.create_order(auth_token, ingredient_ids[:2])
        assert response.status_code == 200
        js = response.json()
        assert js.get("success") is True
        assert "order" in js

    @allure.step('Создание заказа неавторизованным пользователем')
    @allure.description('Проверка кода и ответа')
    def test_create_order_unauthorized(self, ingredient_ids):
        response = OrderMethods.create_order(token="", ingredients=ingredient_ids[:1])
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.step('Создание заказа без ингредиентов')
    @allure.description('Проверка кода и ответа')
    def test_create_order_no_ingredients(self, auth_token):
        response = OrderMethods.create_order(auth_token, [])
        assert response.status_code == 400
        assert response.json().get("message") == "Ingredient ids must be provided"

    @allure.step('Создание заказа с невалидным хешом игредиента')
    @allure.description('Проверка кода и ответа')
    def test_create_order_invalid_hash(self, auth_token):
        response = OrderMethods.create_order(auth_token, ["invalid_id"])
        assert response.status_code == 500
