import requests
from data import Url
import allure

class IngredientMethods:
    @staticmethod
    @allure.step('Получение списка ингредиентов')
    def get_all_ingredients():
        return requests.get(Url.GET_INGREDIENTS_URL)