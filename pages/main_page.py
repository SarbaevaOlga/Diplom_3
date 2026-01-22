import allure

from .base_page import BaseScreen
from utils.application_data import ApplicationURLs
from locators.main_page_locators import MainScreenSelectors


class MainScreen(BaseScreen):
    @allure.step("Открыть главный экран")
    def open_main_screen(self):
        self.navigate_to_url(ApplicationURLs.HOME_PAGE)

    @allure.step("Дождаться загрузки экрана")
    def wait_for_screen_load(self):
        self.wait_for_element_hidden(MainScreenSelectors.MODAL_BACKDROP, timeout=20)

    @allure.step("Проверить открытие главного экрана")
    def is_main_screen_displayed(self):
        return self.get_current_url() == ApplicationURLs.HOME_PAGE

    @allure.step("Перейти в конструктор")
    def navigate_to_builder(self):
        self.scroll_to_element(MainScreenSelectors.BUILDER_LINK)
        self.wait_for_element_clickable(MainScreenSelectors.BUILDER_LINK)
        self.click_element(MainScreenSelectors.BUILDER_LINK)

    @allure.step("Перейти в ленту заказов")
    def navigate_to_orders_feed(self):
        self.wait_for_element_hidden(MainScreenSelectors.MODAL_CONTAINER)
        self.click_element(MainScreenSelectors.ORDERS_FEED_LINK)

    @allure.step("Выбрать ингредиент")
    def select_ingredient(self):
        self.scroll_to_element(MainScreenSelectors.SPECIAL_BUN)
        self.wait_for_element_clickable(MainScreenSelectors.SPECIAL_BUN)
        self.click_element(MainScreenSelectors.SPECIAL_BUN)

    @allure.step("Закрыть модальное окно")
    def close_ingredient_modal(self):
        self.click_element(MainScreenSelectors.MODAL_CLOSE)

    @allure.step("Проверить открытие модального окна")
    def is_modal_displayed(self):
        return self.is_element_displayed(MainScreenSelectors.DETAILS_MODAL)

    @allure.step("Проверить закрытие модального окна")
    def is_modal_closed(self):
        return self.wait_for_element_hidden(MainScreenSelectors.DETAILS_MODAL)

    @allure.step("Ожидание скрытия оверлея")
    def wait_for_backdrop_hidden(self):
        self.wait_for_element_hidden(MainScreenSelectors.MODAL_BACKDROP)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_count(self):
        count_text = self.get_element_text(MainScreenSelectors.ITEM_QUANTITY)
        return int(count_text)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        source_element = self.wait_for_element_visible(MainScreenSelectors.SPECIAL_BUN)
        target_element = self.wait_for_element_visible(MainScreenSelectors.CONSTRUCTOR_AREA)
        self.perform_drag_and_drop(source_element, target_element)

    @allure.step("Создать заказ")
    def create_new_order(self):
        self.wait_for_element_hidden(MainScreenSelectors.LOADING_INDICATOR)
        self.click_element(MainScreenSelectors.CREATE_ORDER_BUTTON)

    @allure.step("Закрыть окно подтверждения заказа")
    def close_order_confirmation(self):
        self.wait_for_element_hidden(MainScreenSelectors.LOADING_INDICATOR)
        self.wait_for_backdrop_hidden()
        self.wait_for_element_visible(MainScreenSelectors.ORDER_NUMBER_DISPLAY)
        self.click_element(MainScreenSelectors.MODAL_CLOSE)

    @allure.step("Получить номер созданного заказа")
    def get_created_order_number(self):
        self.wait_for_backdrop_hidden()
        order_number_text = self.get_element_text(MainScreenSelectors.ORDER_NUMBER_DISPLAY)
        return int(order_number_text)