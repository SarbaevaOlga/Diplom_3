import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginScreen
from utils.application_data import ApplicationURLs, generate_customer_profile


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        browser_instance = webdriver.Chrome()
        browser_instance.maximize_window()
        driver_instance.get(ApplicationURLs.HOME_PAGE)
    elif request.param == "firefox":
        browser_instance = webdriver.Firefox()
        browser_instance.maximize_window()
        browser_instance.get(ApplicationURLs.HOME_PAGE)
    
    yield browser_instance
    browser_instance.quit()


@pytest.fixture(scope="function")
def setup_test_customer():
    customer_data = generate_customer_profile()

    register_response = requests.post(ApplicationURLs.USER_REGISTRATION, json=customer_data)
    access_token = register_response.json()["accessToken"]

    customer_data["token"] = f"Bearer {access_token}"

    yield customer_data

    headers = {"Authorization": customer_data["token"]}
    requests.delete(ApplicationURLs.USER_PROFILE, headers=headers)


@pytest.fixture(scope="function")
def authenticated_user(driver, setup_test_customer):
    login_screen = LoginScreen(driver)
    login_screen.open_login_screen()
    login_screen.perform_login(setup_test_customer["email"], setup_test_customer["password"])
    return driver