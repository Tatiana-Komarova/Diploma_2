
class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    CREATE_USER_URL = f"{BASE_URL}/api/auth/register"
    LOGIN_USER_URL = f"{BASE_URL}/api/auth/login"
    GET_UPDATE_USER_URL = f"{BASE_URL}/api/auth/user"
    CREATE_ORDER_URL = f"{BASE_URL}/api/orders"
    GET_ALL_ORDERS_URL = f"{BASE_URL}/api/orders/all"
    GET_USER_ORDER_URL = f"{BASE_URL}/api/orders"
    GET_INGREDIENTS_URL = f"{BASE_URL}/api/ingredients"
    DELETE_USER_URL = f"{BASE_URL}/api/auth/user"
