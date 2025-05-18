import pytest
import allure
from methods.user_methods import UserMethods
import uuid

class TestUserUpdate:
    @allure.step('Обновление информации о пользователе')
    @allure.description('Проверка кода и ответа')
    @pytest.mark.parametrize("payload", [{"name": "NewSuperHero"}, {"email": None}, {"password": "NewHero098"}])
    def test_update_user_authorized(self, auth_token, payload):
        if "email" in payload and payload["email"] is None:
            payload = {"email": f"{uuid.uuid4().hex}@example.com"}
        response = UserMethods.update_user_info(auth_token, payload)
        assert response.status_code == 200
        body = response.json()
        assert body.get("success") is True

        if "user" in body:
            user = body["user"]
        else:
            get = UserMethods.get_user_info(auth_token)
            assert get.status_code == 200
            user = get.json()["user"]
        for k, v in payload.items():
            if k != "password":
                assert user[k] == v


    @allure.step('Проверка обновления информации неавторизованного пользователя')
    @allure.description('Проверка кода и ответа')
    def test_update_user_unauthorized(self):
        response = UserMethods.update_user_info(token="", body={"name": "H"})
        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"