from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as LPLocs
from data import TestWaitTime as TWTime
from urls import Url
import allure

class LoginPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        self.go_to_page(Url.login_page)

    @allure.step('Ожидание загрузки страницы авторизации')
    def wait_load_login_page(self, wait_time=TWTime.page):
        self.wait_for_visibility_element(LPLocs.login_page_header, wait_time)

    @allure.step('Заполняем поле "Email"')
    def set_email_placeholder(self, email):
        self.set_data(LPLocs.field_email, email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password_placeholder(self, password):
        self.set_data(LPLocs.field_password, password)

    @allure.step('Нажимаем кнопку "Войти"')
    def click_button_enter(self):
        self.click_on_element(LPLocs.button_login)

    @allure.step('Авторизация пользователя')
    @allure.description('Переход на страницу авторизации с ожиданием её загрузки, и авторизация пользователя')
    def user_login(self, email, password, wait_time=TWTime.page):
        self.open_login_page()
        self.wait_load_login_page(wait_time)
        self.set_email_placeholder(email)
        self.set_password_placeholder(password)
        self.click_button_enter()
