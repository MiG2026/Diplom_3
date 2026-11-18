import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import UserLoginData as ULData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from urls import Url

#запуск браузера
@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    if driver_class == webdriver.Chrome:
        options = Options()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
    elif driver_class == webdriver.Firefox:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
    driver.get(Url.base_url)
    yield driver
    driver.quit()

#запуск браузера с переходом на главную страницу
@pytest.fixture
def driver_main_page(driver):
    m_page = MainPage(driver)
    m_page.wait_open_and_load_main_page(20)

    return m_page

#запуск браузера с авторизацией
@pytest.fixture
def driver_with_auth(driver):
    l_page = LoginPage(driver)
    m_page = MainPage(driver)
    l_page.user_login(ULData.email, ULData.password, 15)
    m_page.wait_load_main_page(10)

    return driver
