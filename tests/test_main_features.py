import allure
import pytest

from pages.login_page import LoginScreen
from pages.main_page import MainScreen
from pages.orders_page import OrdersScreen


@allure.feature("Основная функциональность приложения")
class TestCoreFunctionality:

    @allure.title("Переход в конструктор через навигацию")
    def test_navigation_to_builder_works_correctly(self, driver):
        main_screen = MainScreen(driver)
        orders_screen = OrdersScreen(driver)

        orders_screen.open_orders_screen()
        main_screen.wait_for_screen_load()

        main_screen.navigate_to_builder()

        assert main_screen.is_main_screen_displayed()

    @allure.title("Переход в ленту заказов через навигацию")
    def test_navigation_to_orders_feed_works_correctly(self, driver):
        main_screen = MainScreen(driver)
        orders_screen = OrdersScreen(driver)

        main_screen.open_main_screen()
        main_screen.wait_for_screen_load()

        main_screen.navigate_to_orders_feed()

        assert orders_screen.is_orders_screen_displayed()

    @allure.title("Открытие деталей ингредиента")
    def test_ingredient_details_modal_opens_on_click(self, driver):
        main_screen = MainScreen(driver)

        main_screen.open_main_screen()
        main_screen.wait_for_screen_load()

        main_screen.select_ingredient()

        assert main_screen.is_modal_displayed()

    @allure.title("Закрытие модального окна")
    def test_modal_window_closes_with_close_button(self, driver):
        main_screen = MainScreen(driver)

        main_screen.open_main_screen()
        main_screen.wait_for_screen_load()

        main_screen.select_ingredient()
        main_screen.close_ingredient_modal()

        assert main_screen.is_modal_closed()

    @allure.title("Счетчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_updates_on_addition(self, driver):
        main_screen = MainScreen(driver)

        main_screen.open_main_screen()
        main_screen.wait_for_screen_load()

        initial_count = main_screen.get_ingredient_count()

        main_screen.select_ingredient()
        main_screen.add_ingredient_to_constructor()

        updated_count = main_screen.get_ingredient_count()

        assert updated_count > initial_count