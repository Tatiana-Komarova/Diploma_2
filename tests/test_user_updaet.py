import pytest
import allure
from methods.user_methods import UserMethods
import uuid

class TestUserUpdate:
    @allure.title('Обновление информации о пользователе')
    @allure.step('Проверка кода и ответа')
    @pytest.mark.parametrize("field, value, verify", [
        ("name", "NewSuperHero", True),
        ("email", f"{uuid.uuid4().hex}@example.com", True),
        ("password", "NewHero098", False),
    ])
    def test_update_user_authorized(self, auth_token, field, value, verify):
        payload = {field: value}
        response = UserMethods.update_user_info(auth_token, payload)
        assert response.status_code == 200
        body = response.json()
        assert body.get("success") is True

        if verify:
            get_response = UserMethods.get_user_info(auth_token)
            assert get_response.status_code == 200
            user = get_response.json()["user"]
            assert user[field] == value


    @allure.title('Проверка обновления информации неавторизованного пользователя')
    @allure.step('Проверка кода и ответа')
    def test_update_user_unauthorized(self):
        response = UserMethods.update_user_info(token="", body={"name": "H"})
        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"