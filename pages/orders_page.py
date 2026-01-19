import allure

from .base_page import BaseScreen
from utils.application_data import ApplicationURLs
from locators.orders_page_locators import OrdersScreenSelectors


class OrdersScreen(BaseScreen):
    @allure.step("Открыть страницу ленты заказов")
    def open_orders_feed(self):
        self.navigate_to_url(ApplicationURLs.ORDERS_FEED)

    @allure.step("Проверить открытие страницы заказов")
    def is_orders_screen_displayed(self):
        return self.get_current_url() == ApplicationURLs.ORDERS_FEED

    @allure.step("Ожидание скрытия оверлея")
    def wait_for_overlay_disappear(self):
        self.wait_for_element_hidden(OrdersScreenSelectors.MODAL_BACKDROP, timeout=15)


    @allure.step("Получить общее количество заказов")
    def get_total_orders_total(self):
        self.wait_for_overlay_disappear()
        count_text = self.get_element_text(OrdersScreenSelectors.ALL_TIME_ORDERS)
        return int(count_text)

    @allure.step("Получить количество заказов за сегодня")
    def get_todays_orders_total(self):
        self.wait_for_overlay_disappear()
        count_text = self.get_element_text(OrdersScreenSelectors.TODAY_ORDERS)
        return int(count_text)

    @allure.step("Ожидание появления активных заказов")
    def wait_for_active_orders(self):
        self.wait_for_element_attribute(
            OrdersScreenSelectors.ACTIVE_ORDERS_LIST, 
            'class',  
            'class', 
            'text text_type_digits-default mb-2'
        )

    @allure.step("Получить номер активного заказа")
    def get_current_order_id(self):
        self.wait_for_backdrop_hidden()
        order_text = self.get_element_text(OrdersScreenSelectors.ACTIVE_ORDERS_LIST)
        return int(order_text)

    @allure.step("Дождаться загрузки страницы заказов")
    def for_screen_ready(self):
        self.wait_for_element_visible(OrdersScreenSelectors.ALL_TIME_ORDERS)
        self.scroll_to_element(OrdersScreenSelectors.ALL_TIME_ORDERS)