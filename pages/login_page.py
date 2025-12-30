import allure

from .base_page import BaseScreen
from utils.application_data import ApplicationURLs
from locators.login_page_locators import LoginScreenSelectors
from locators.main_page_locators import MainScreenSelectors


class LoginScreen(BaseScreen):
    @allure.step("Открыть экран авторизации")
    def open_login_screen(self):
        self.navigate_to_url(ApplicationURLs.LOGIN_PAGE)

    @allure.step("Выполнить авторизацию")
    def perform_login(self, email, password):
        self.enter_text(LoginScreenSelectors.EMAIL_INPUT, email)
        self.enter_text(LoginScreenSelectors.PASSWORD_FIELD, password)
        self.wait_for_element_hidden(MainScreenSelectors.LOADING_INDICATOR)
        self.click_element(LoginScreenSelectors.SUBMIT_BUTTON)