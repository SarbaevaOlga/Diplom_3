import allure
import pytest

from pages.main_page import MainPage
from pages.orders_page import OrdersPage


@allure.feature("Отслеживание заказов")
class TestOrderMonitoring:

    @allure.title("Счетчик всех заказов обновляется после создания заказа")
    def test_lifetime_counter_updates_after_order(self, logged_in_user):
        main_page = MainPage(logged_in_user)
        orders_page = OrdersPage(logged_in_user)

        main_page.wait_for_page_loaded()

        main_page.go_to_orders_feed()
        orders_page.wait_for_page_load()
        initial_lifetime_total = orders_page.get_lifetime_orders_total()

        main_page.go_to_constructor()
        main_page.wait_for_page_loaded()

        main_page.drop_ingredient_to_constructor()
        main_page.place_new_order()

        main_page.close_order_modal()

        main_page.go_to_orders_feed()
        final_lifetime_total = orders_page.get_lifetime_orders_total()

        assert final_lifetime_total > initial_lifetime_total

    @allure.title("Счетчик сегодняшних заказов обновляется после создания заказа")
    def test_daily_counter_updates_after_order(self, logged_in_user):
        main_page = MainPage(logged_in_user)
        orders_page = OrdersPage(logged_in_user)

        main_page.wait_for_page_loaded()

        main_page.go_to_orders_feed()
        orders_page.wait_for_page_load()
        initial_daily_total = orders_page.get_daily_orders_total()

        main_page.go_to_constructor()
        main_page.wait_for_page_loaded()

        main_page.drop_ingredient_to_constructor()
        main_page.place_new_order()

        main_page.close_order_modal()

        main_page.go_to_orders_feed()
        final_daily_total = orders_page.get_daily_orders_total()

        assert final_daily_total > initial_daily_total

    @allure.title("Номер заказа отображается в активных заказах")
    def test_order_id_shown_in_current_orders(self, logged_in_user):
        main_page = MainPage(logged_in_user)
        orders_page = OrdersPage(logged_in_user)

        main_page.wait_for_page_loaded()

        main_page.drop_ingredient_to_constructor()
        main_page.place_new_order()

        created_order_id = main_page.get_created_order_id()
        main_page.close_order_modal()

        main_page.go_to_orders_feed()
        orders_page.wait_for_page_load()

        orders_page.wait_for_current_orders()
        current_order_id = orders_page.get_current_order_id()

        assert created_order_id == current_order_id