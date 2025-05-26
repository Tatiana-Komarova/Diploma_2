import pytest
import allure
from methods.user_methods import UserMethods

class TestUserRegistration:
    @allure.title('Успешное создание пользователя')
    @allure.step('Проверка кода и ответа')
    def test_create_user(self, generate_user_data):
        response = UserMethods.create_user(generate_user_data)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title('Проверка создания уже существующего пользователя')
    @allure.step('Проверка кода и ответа')
    def test_create_existing_user(self, generate_user_data):
        body = generate_user_data.copy()
        response_1 = UserMethods.create_user(body)
        assert response_1.status_code == 200
        response_2 = UserMethods.create_user(body)
        assert response_2.status_code == 403
        assert response_2.json().get("message", "") == "User already exists"

    @allure.title('Создание пользователя, если одно из обязательных полей отсутствует')
    @allure.step('Проверка кода и ответа')
    @pytest.mark.parametrize("missed_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, generate_user_data, missed_field):
        data = generate_user_data.copy()
        data.pop(missed_field)
        response = UserMethods.create_user(data)
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"

