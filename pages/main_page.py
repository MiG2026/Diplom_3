from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as BPLocs
from locators.main_page_locators import MainPageLocators as MPLocs
from data import TestWaitTime as TWTime
from urls import Url
import allure

class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.go_to_page(Url.main_page)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_load_main_page(self, wait_time=TWTime.page):
        self.wait_for_visibility_element(MPLocs.main_page_header, wait_time)

    @allure.step('Открываем главную страницу и ожидаем её загрузки')
    def wait_open_and_load_main_page(self, wait_time=TWTime.page):
        self.open_main_page()
        self.wait_load_main_page(wait_time)

    @allure.step('Нажимаем на кнопку "Лента Заказов" в шапке страницы')
    def click_button_feed(self):
        self.click_on_element(BPLocs.header_button_feed)

    @allure.step('Проверяем переход на страницу "Лента Заказов"')
    def check_open_feed_page(self):
        actual_url = self.get_page_url()
        expect_url = Url.feed_page
        return actual_url == expect_url

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self):
        self.click_on_element(MPLocs.ingredient)

    @allure.step('Проверяем появление окна "Детали ингредиента"')
    def check_open_window_ingred_details(self, wait_time=TWTime.window):
        return self.check_element_is_displayed(MPLocs.window_ingr_details, wait_time)

    @allure.step('Проверяем закрытие окна "Детали ингредиента"')
    def check_close_window_ingred_details(self, wait_time=TWTime.invisible):
        return self.check_element_not_is_displayed(MPLocs.window_ingr_details, wait_time)

    @allure.step('Нажимаем на кнопку "Х" в окне "Детали ингредиента"')
    def click_button_x(self):
        self.click_on_element(MPLocs.button_close_x)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.wait_for_visibility_element(MPLocs.ingredient, 10)
        self.drag_and_drop_element(MPLocs.ingredient, MPLocs.burger_constructor)

    @allure.step('Получаем значение счётчика ингредиента')
    def get_ingredient_counter(self):
        """Возвращает значение счётчика ингредиента (0, если счётчик скрыт или отсутствует)."""
        counters = self.get_elements(MPLocs.counter_ingredient)
        if not counters:
            return 0
        counter = counters[0]
        if not counter.is_displayed():
            return 0
        text = counter.text.strip()
        return int(text) if text else 0

    @allure.step('Ждём, что счётчик ингредиента станет равен {expected}')
    def wait_counter_ingredient_equals(self, expected, timeout=10):
        return self.wait_for_condition(
            lambda d: self.get_ingredient_counter() == expected,
            timeout,
            message=f'Счётчик ингредиента не стал равен {expected}')

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_on_element(MPLocs.button_create_order)

    @allure.step('Ожидаем появления окна id заказа')
    def wait_load_window_order_details(self, wait_time=TWTime.window):
        self.wait_for_visibility_element(MPLocs.id_order, wait_time)

    @allure.step('Ожидаем исчезновения затемнения')
    def wait_invisible_overlay(self, wait_time=TWTime.invisible):
        self.check_element_not_is_displayed(MPLocs.overlay, wait_time)

    @allure.step('Получаем id заказа')
    def get_id_order(self, wait_time=TWTime.visible):
        self.wait_for_visibility_element(MPLocs.id_order, wait_time)
        return self.get_text(MPLocs.id_order)

    @allure.step('Создаем заказ')
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_button_create_order()

    @allure.step('Добавляем соус в заказ')
    def add_sauce_to_order(self):
        self.wait_for_visibility_element(MPLocs.sauce_spicy, 10)
        self.drag_and_drop_element(MPLocs.sauce_spicy, MPLocs.burger_constructor)

    @allure.step('Получаем значение счётчика соуса')
    def get_sauce_counter(self):
        """Возвращает значение счётчика соуса (0, если счётчик скрыт или отсутствует)."""
        counters = self.get_elements(MPLocs.counter_sauce_spicy)
        if not counters:
            return 0
        text = (counters[0].get_attribute('textContent') or '').strip()
        return int(text) if text else 0

    @allure.step('Ждём, что счётчик соуса станет равен {expected}')
    def wait_sauce_counter_equals(self, expected, timeout=10):
        return self.wait_for_condition(
            lambda d: self.get_sauce_counter() == expected,
            timeout,
            message=f'Счётчик соуса не стал равен {expected}')
