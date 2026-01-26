
class MainScreenSelectors:
    # навигационные элементы
    BUILDER_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")

    # элементы конструктора
    SPECIAL_BUN = (By.XPATH, ".//*[text()='Флюоресцентная булка R2-D3']")
    ITEM_QUANTITY = (By.XPATH, ".//*[@class='counter_counter__num__3nue1']")

    # модальные окна
    DETAILS_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    MODAL_BACKDROP = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
    LOADING_INDICATOR = (By.XPATH, "//img[@alt ='loading animation']")
    MODAL_CONTAINER = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")

    # область конструктора
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")

    # оформление заказа
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_DISPLAY = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")