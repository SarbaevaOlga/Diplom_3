import random
import string
import time


class ApplicationURLs:
    # основные страницы приложения
    HOME_PAGE = 'https://stellarburgers.education-services.ru/'
    LOGIN_PAGE = f'{HOME_PAGE}login'
    ORDERS_FEED = f'{HOME_PAGE}feed'

    # API endpoints
    USER_REGISTRATION = f'{HOME_PAGE}api/auth/register'
    USER_PROFILE = f'{HOME_PAGE}api/auth/user'


def generate_customer_profile():
    """Генератор тестовых профилей клиентов"""
    timestamp = int(time.time())
    random_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    
    customer_name = f"Customer{timestamp}"
    customer_email = f"customer{timestamp}@testmail.org"
    customer_password = f"SecurePass{timestamp}{random_id}!"
    
    return {
        "email": customer_email,
        "password": customer_password,
        "name": customer_name
    }