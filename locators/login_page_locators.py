from selenium.webdriver.common.by import By


class LoginPageLocators():
    #заголовок страницы авторизации
    login_page_header = (By.XPATH, ".//h2[text()='Вход']")
    #поле email
    field_email = (By.XPATH, ".//input[@name='name']")
    #поле пароль
    field_password = (By.XPATH, ".//input[@name='Пароль']")
    #кнопка'Войти'
    button_login = (By.XPATH, ".//button[text()='Войти']")
