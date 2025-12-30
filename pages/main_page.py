import allure

from .base_page import BasePage
from utils.application_data import AppUrls
from locators.main_page_locators import MainPageElements


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.go_to_page(AppUrls.MAIN_PAGE)

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_loaded(self):
        self.wait_until_hidden(MainPageElements.MODAL_OVERLAY, timeout=20)

    @allure.step("Проверить открытие главной страницы")
    def verify_main_page_opened(self):
        return self.get_page_url() == AppUrls.MAIN_PAGE

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.scroll_into_view(MainPageElements.CONSTRUCTOR_LINK)
        self.wait_until_clickable(MainPageElements.CONSTRUCTOR_LINK)
        self.click_on_element(MainPageElements.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def go_to_orders_feed(self):
        self.wait_until_hidden(MainPageElements.MODAL_WRAPPER)
        self.click_on_element(MainPageElements.ORDERS_FEED_LINK)

    @allure.step("Выбрать ингредиент")
    def pick_ingredient(self):
        self.scroll_into_view(MainPageElements.FLUORESCENT_BUN)
        self.wait_until_clickable(MainPageElements.FLUORESCENT_BUN)
        self.click_on_element(MainPageElements.FLUORESCENT_BUN)

    @allure.step("Закрыть модальное окно")
    def close_details_modal(self):
        self.click_on_element(MainPageElements.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить открытие модального окна")
    def check_modal_visible(self):
        return self.check_element_visibility(MainPageElements.DETAILS_MODAL_WINDOW)

    @allure.step("Проверить закрытие модального окна")
    def check_modal_closed(self):
        return self.wait_until_hidden(MainPageElements.DETAILS_MODAL_WINDOW)

    @allure.step("Ожидание скрытия оверлея")
    def wait_for_overlay_disappear(self):
        self.wait_until_hidden(MainPageElements.MODAL_OVERLAY)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        counter_text = self.get_text_content(MainPageElements.QUANTITY_INDICATOR)
        return int(counter_text)

    @allure.step("Добавить ингредиент в конструктор")
    def drop_ingredient_to_constructor(self):
        source_item = self.wait_until_visible(MainPageElements.FLUORESCENT_BUN)
        target_zone = self.wait_until_visible(MainPageElements.CONSTRUCTOR_ZONE)
        self.drag_and_drop_element(source_item, target_zone)

    @allure.step("Создать заказ")
    def place_new_order(self):
        self.wait_until_hidden(MainPageElements.LOADING_SPINNER)
        self.click_on_element(MainPageElements.PLACE_ORDER_BUTTON)

    @allure.step("Закрыть окно подтверждения заказа")
    def close_order_modal(self):
        self.wait_until_hidden(MainPageElements.LOADING_SPINNER)
        self.wait_for_overlay_disappear()
        self.wait_until_visible(MainPageElements.ORDER_ID_DISPLAY)
        self.click_on_element(MainPageElements.MODAL_CLOSE_BUTTON)

    @allure.step("Получить номер созданного заказа")
    def get_created_order_id(self):
        self.wait_for_overlay_disappear()
        order_id_text = self.get_text_content(MainPageElements.ORDER_ID_DISPLAY)
        return int(order_id_text)