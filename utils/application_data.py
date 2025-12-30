import random
import string
import time


class AppUrls:
    # основные страницы приложения
    MAIN_PAGE = 'https://stellarburgers.education-services.ru/'
    LOGIN_PAGE = f'{MAIN_PAGE}login'
    ORDERS_PAGE = f'{MAIN_PAGE}feed'

    # API endpoints
    REGISTRATION_ENDPOINT = f'{MAIN_PAGE}api/auth/register'
    USER_DATA_ENDPOINT = f'{MAIN_PAGE}api/auth/user'


def create_test_customer():
    """Генератор тестовых профилей пользователей"""
    current_timestamp = int(time.time())
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    
    user_name = f"User{current_timestamp}"
    user_email = f"user{current_timestamp}@testmail.org"
    user_password = f"SecurePass{current_timestamp}{random_string}!"
    
    return {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }