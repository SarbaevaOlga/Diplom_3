from selenium.webdriver.common.by import By


class OrdersScreenSelectors:
    # счетчики заказов
    ALL_TIME_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # текущие заказы
    ACTIVE_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    MODAL_BACKDROP = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")