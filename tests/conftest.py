import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from utils.application_data import AppUrls, create_test_customer


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        browser_instance = webdriver.Chrome()
        browser_instance.maximize_window()
        browser_instance.get(AppUrls.MAIN_PAGE)
    elif request.param == "firefox":
        browser_instance = webdriver.Firefox()
        browser_instance.maximize_window()
        browser_instance.get(AppUrls.MAIN_PAGE)
    
    yield browser_instance
    browser_instance.quit()


@pytest.fixture(scope="function")
def prepare_test_user():
    user_credentials = create_test_customer()

    registration_result = requests.post(AppUrls.REGISTRATION_ENDPOINT, json=user_credentials)
    auth_token = registration_result.json()["accessToken"]

    user_credentials["auth_header"] = f"Bearer {auth_token}"

    yield user_credentials

    auth_headers = {"Authorization": user_credentials["auth_header"]}
    requests.delete(AppUrls.USER_DATA_ENDPOINT, headers=auth_headers)


@pytest.fixture(scope="function")
def logged_in_user(browser, prepare_test_user):
    login_page = LoginPage(browser)
    login_page.go_to_login_page()
    login_page.authenticate_user(prepare_test_user["email"], prepare_test_user["password"])
    return browser