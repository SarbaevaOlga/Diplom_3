import allure

from pages.base_page import BasePage
from utils.application_data import AppUrls
from locators.login_page_locators import LoginPageElements
from locators.main_page_locators import MainPageElements


class LoginPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def go_to_login_page(self):
        self.go_to_page(AppUrls.LOGIN_PAGE)

    @allure.step("Выполнить авторизацию")
    def authenticate_user(self, user_email, user_password):
        self.fill_input_field(LoginPageElements.EMAIL_FIELD, user_email)
        self.fill_input_field(LoginPageElements.PASSWORD_FIELD, user_password)
        self.wait_until_hidden(MainPageElements.LOADING_SPINNER)
        self.click_on_element(LoginPageElements.LOGIN_BUTTON)