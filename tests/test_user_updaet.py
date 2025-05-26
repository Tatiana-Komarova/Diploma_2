import pytest
import allure
from methods.user_methods import UserMethods
import uuid

class TestUserUpdate:
    @allure.title('Обновление имени и email пользователя')
    @allure.step('Проверка кода и ответа')
    @pytest.mark.parametrize("field, value", [
        ("name", "NewSuperHero"),
        ("email", f"{uuid.uuid4().hex}@example.com")
    ])
    def test_update_user_name_email_authorized(self, auth_token, field, value):
        payload = {field: value}
        response = UserMethods.update_user_info(auth_token, payload)
        assert response.status_code == 200
        assert response.json().get("success") is True

        get_response = UserMethods.get_user_info(auth_token)
        assert get_response.status_code == 200
        user = get_response.json()["user"]
        assert user[field] == value


    @allure.title('Обновление пароля и авторизация с новым паролем')
    @allure.step('Проверка кода и ответа')
    def test_update_user_password(self, auth_token, registered_user):
        new_pass = "NewHero098"

        response = UserMethods.update_user_info(auth_token, {"password": new_pass})
        assert response.status_code == 200
        assert response.json().get("success") is True

        login = UserMethods.login_user(registered_user["email"], new_pass)
        assert login.status_code == 200
        assert "accessToken" in login.json()


    @allure.title('Проверка обновления информации неавторизованного пользователя')
    @allure.step('Проверка кода и ответа')
    def test_update_user_unauthorized(self):
        response = UserMethods.update_user_info(token="", body={"name": "H"})
        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"