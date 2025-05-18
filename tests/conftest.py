import pytest
from methods.user_methods import UserMethods
from methods.ingredient_methods import IngredientMethods
import allure
from faker import Faker
fake = Faker()

@pytest.fixture
def generate_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()}

@pytest.fixture(scope="function")
def registered_user(generate_user_data):
    response = UserMethods.create_user(generate_user_data)
    assert response.status_code == 200
    return generate_user_data

@pytest.fixture
def auth_token(registered_user):
    response = UserMethods.login_user(registered_user["email"], registered_user["password"])
    assert response.status_code == 200, 403
    token = response.json().get("accessToken")
    assert token
    return token

@pytest.fixture
def ingredient_ids():
    response = IngredientMethods.get_all_ingredients()
    assert response.status_code == 200, response.text
    data = response.json().get("data", [])
    return [item["_id"] for item in data]