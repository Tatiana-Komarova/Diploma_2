import pytest
import allure
from methods.user_methods import UserMethods

class TestUserAuth:
    @allure.title('Проверка успешной авторизации')
    @allure.step('Проверка кода и ответа')
    def test_login_success(self, registered_user):
        response = UserMethods.login_user(registered_user["email"], registered_user["password"])
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title('Авторизация с неверными данными')
    @allure.step('Проверка кода и ответа')
    @pytest.mark.parametrize("email,password", [("wrong@example.com", "wrongpass"), ("", "")])
    def test_login_wrong_credentials(self, email, password):
        response = UserMethods.login_user(email, password)
        assert response.status_code == 401
        assert response.json().get("message") == "email or password are incorrect"
