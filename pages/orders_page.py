import allure

from .base_page import BasePage
from utils.application_data import AppUrls
from locators.orders_page_locators import OrdersPageElements


class OrdersPage(BasePage):
    @allure.step("Открыть страницу ленты заказов")
    def open_orders_feed(self):
        self.go_to_page(AppUrls.ORDERS_PAGE)

    @allure.step("Проверить открытие страницы заказов")
    def verify_orders_page_opened(self):
        return self.get_page_url() == AppUrls.ORDERS_PAGE

    @allure.step("Ожидание скрытия оверлея")
    def wait_for_overlay_disappear(self):
        self.wait_until_hidden(OrdersPageElements.MODAL_OVERLAY, timeout=15)

    @allure.step("Получить общее количество заказов")
    def get_lifetime_orders_total(self):
        self.wait_for_overlay_disappear()
        count_value = self.get_text_content(OrdersPageElements.LIFETIME_ORDERS_COUNT)
        return int(count_value)

    @allure.step("Получить количество заказов за сегодня")
    def get_daily_orders_total(self):
        self.wait_for_overlay_disappear()
        count_value = self.get_text_content(OrdersPageElements.DAILY_ORDERS_COUNT)
        return int(count_value)

    @allure.step("Ожидание появления активных заказов")
    def wait_for_current_orders(self):
        self.wait_for_attribute_value(
            OrdersPageElements.CURRENT_ORDERS, 
            'class', 
            'text text_type_digits-default mb-2'
        )

    @allure.step("Получить номер активного заказа")
    def get_current_order_id(self):
        self.wait_for_overlay_disappear()
        order_text = self.get_text_content(OrdersPageElements.CURRENT_ORDERS)
        return int(order_text)

    @allure.step("Дождаться загрузки страницы заказов")
    def wait_for_page_load(self):
        self.wait_until_visible(OrdersPageElements.LIFETIME_ORDERS_COUNT)
        self.scroll_into_view(OrdersPageElements.LIFETIME_ORDERS_COUNT)