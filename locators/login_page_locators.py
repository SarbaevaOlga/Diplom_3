from selenium.webdriver.common.by import By


class LoginScreenSelectors:
    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")