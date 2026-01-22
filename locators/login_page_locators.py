from selenium.webdriver.common.by import By


class LoginScreenSelectors:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")