import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Ожидание видимости элемента")
    def wait_until_visible(self, locator, wait_time=20):
        return WebDriverWait(self.browser, wait_time).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_until_clickable(self, locator):
        return WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        element = self.wait_until_clickable(locator)
        element.click()

    @allure.step("Получение текста элемента")
    def get_text_content(self, locator):
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
        element = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание скрытия элемента")
    def wait_for_element_hidden(self, locator, wait_time=20):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетаскивание элемента")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text_content, wait_time=20):
        element = self.wait_until_visible(locator, wait_time)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание атрибута элемента")
    def wait_for_attribute_value(self, locator, attribute, expected_value, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, expected_value)
        )