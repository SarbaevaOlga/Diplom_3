import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BaseScreen:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step("Проверка видимости элемента")
    def is_element_displayed(self, locator):
        return self.wait_for_element_visible(locator).is_displayed()

    @allure.step("Открытие страницы")
    def navigate_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание скрытия элемента")
    def wait_for_element_hidden(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетаскивание элемента")
    def perform_drag_and_drop(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text, timeout=20):
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание атрибута элемента")
    def wait_for_element_attribute(self, locator, attribute, expected_value, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, expected_value)
        )