from selenium.webdriver.common.by import By


class MainPageLocators():
    #заголовок главной страницы
    main_page_header = (By.XPATH, ".//h1[text()='Соберите бургер']")
    #кнопка "Оформить заказ"(появляется после авторизации)
    button_create_order = (By.XPATH, ".//button[text()='Оформить заказ']")
    #идентификатор заказа
    id_order = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    #затемнение экрана
    overlay = (By.XPATH, "(.//div[@class='Modal_modal_overlay__x2ZCr'])[2]")
    #ингредиент "Флюоресцентная булка R2-D3"
    ingredient = (By.XPATH, "//a[@draggable='true' and .//p[text()='Флюоресцентная булка R2-D3']]")
    #окно "Детали ингредиента"
    window_ingr_details = (By.XPATH, ".//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")
    #кнопка "Х" закрывает детали ингредиента
    button_close_x = (By.XPATH, "(.//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    #счетчик ингредиента
    counter_ingredient = (By.XPATH, "(.//p[@class='counter_counter__num__3nue1'])[1]")
    #конструктор бургера
    burger_constructor = (By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    #соус "Соус Spicy-X"
    sauce_spicy = (By.XPATH, "//a[@draggable='true' and .//p[text()='Соус Spicy-X']]")
    # счётчик соуса "Соус Spicy-X"
    counter_sauce_spicy = (By.XPATH, "(//a[.//p[text()='Соус Spicy-X']]//p[@class='counter_counter__num__3nue1'])[1]")