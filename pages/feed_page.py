from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as BPLocs
from locators.feed_page_locators import FeedPageLocators as FPLocs
from data import TestWaitTime as TWTime
from urls import Url
import allure
from selenium.webdriver.support.ui import WebDriverWait


class FeedPage(BasePage):

    @allure.step('Открываем страницу "Лента Заказов"')
    def open_feed_page(self):
        self.go_to_page(Url.feed_page)

    @allure.step('Ожидание загрузки страницы "Лента Заказов"')
    def wait_load_feed_page(self, wait_time=TWTime.page):
        self.wait_for_visibility_element(FPLocs.feed_page_header, wait_time)

    @allure.step('Открываем главную страницу и ожидаем её загрузки')
    def wait_open_and_load_feed_page(self, wait_time=TWTime.page):
        self.open_feed_page()
        self.wait_load_feed_page(wait_time)

    @allure.step('Нажимаем на кнопку "Конструктор" в шапке страницы')
    def click_button_builder(self):
        self.click_on_element(BPLocs.header_button_builder)

    @allure.step('Проверяем переход на главную страницу')
    def check_open_main_page(self):
        actual_url = self.get_page_url()
        expect_url = Url.main_page
        return actual_url == expect_url

    @allure.step('Проверяем счетчик «Выполнено за всё время»')
    def check_counter_completed_all_time(self):
        count = self.get_text(FPLocs.counter_completed_all_time)
        return int(count)

    @allure.step('Проверяем счетчик «Выполнено за сегодня»')
    def check_counter_completed_today(self):
        count = self.get_text(FPLocs.counter_completed_today)
        return int(count)

    @staticmethod
    def _normalize_order_id(value):
        s = str(value).strip()
        return s.lstrip('0') or '0'

    @allure.step('Получаем список ID заказов в разделе «В работе»')
    def get_order_ids_in_work(self):
        elements = self.driver.find_elements(*FPLocs.section_in_work)
        return [
        self._normalize_order_id(el.text)
        for el in elements
        if el.text.strip()
        ]

    @allure.step('Ждём появления заказа {expected_id} в разделе «В работе»')
    def wait_order_appears_in_work(self, expected_id, timeout=20):
        expected_norm = self._normalize_order_id(expected_id)
        def _check(driver):
            ids = self.get_order_ids_in_work()
            return expected_norm in ids
        return WebDriverWait(self.driver, timeout).until(_check)