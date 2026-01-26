import allure
import pytest

from pages.main_page import MainScreen
from pages.orders_page import OrdersScreen


@allure.feature("Отслеживание заказов")
class TestOrderTracking:

    @allure.title("Счетчик всех заказов обновляется после создания заказа")
    def test_total_orders_counter_updates_after_order_creation(self, authenticated_user):
        main_screen = MainScreen(authenticated_user)
        orders_screen = OrdersScreen(authenticated_user)

        main_screen.wait_for_screen_load()

        main_screen.navigate_to_orders_feed()
        orders_screen.wait_for_screen_ready()
        initial_total = orders_screen.get_total_orders_count()

        main_screen.navigate_to_builder()
        main_screen.wait_for_screen_load()

        main_screen.add_ingredient_to_constructor()
        main_screen.create_new_order()

        main_screen.close_order_confirmation()

        main_screen.navigate_to_orders_feed()
        final_total = orders_screen.get_total_orders_count()

        assert final_total > initial_total

    @allure.title("Счетчик сегодняшних заказов обновляется после создания заказа")
    def test_todays_orders_counter_updates_after_order_creation(self, authenticated_user):
        main_screen = MainScreen(authenticated_user)
        orders_screen = OrdersScreen(authenticated_user)

        main_screen.wait_for_screen_load()

        main_screen.navigate_to_orders_feed()
        orders_screen.wait_for_screen_ready()
        initial_today = orders_screen.get_todays_orders_count()

        main_screen.navigate_to_builder()
        main_screen.wait_for_screen_load()

        main_screen.add_ingredient_to_constructor()
        main_screen.create_new_order()

        main_screen.close_order_confirmation()

        main_screen.navigate_to_orders_feed()
        final_today = orders_screen.get_todays_orders_count()

        assert final_today > initial_today

    @allure.title("Номер заказа отображается в активных заказах")
    def test_order_number_appears_in_active_orders(self, authenticated_user):
        main_screen = MainScreen(authenticated_user)
        orders_screen = OrdersScreen(authenticated_user)

        main_screen.wait_for_screen_load()

        main_screen.add_ingredient_to_constructor()
        main_screen.create_new_order()

        created_order_number = main_screen.get_created_order_number()
        main_screen.close_order_confirmation()

        main_screen.navigate_to_orders_feed()
        orders_screen.wait_for_screen_ready()

        orders_screen.wait_for_active_orders()
        active_order_number = orders_screen.get_active_order_number()

        assert created_order_number == active_order_number