from selenium.webdriver.common.by import By


class BasePageLocators():
    #кнопка "Конструктор" в шапке страницы
    header_button_builder = (By.XPATH, "(.//p[@class='AppHeader_header__linkText__3q_va ml-2'])[1]")
    #кнопка "Лента Заказов" в шапке страницы
    header_button_feed = (By.XPATH, "(.//p[@class='AppHeader_header__linkText__3q_va ml-2'])[2]")