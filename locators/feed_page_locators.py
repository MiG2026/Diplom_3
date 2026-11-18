from selenium.webdriver.common.by import By


class FeedPageLocators():
    #заголовок страницы заказов
    feed_page_header = (By.XPATH, ".//h1[text()='Лента заказов']")
    #счетчик «Выполнено за всё время»
    counter_completed_all_time = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    #счетчик «Выполнено за сегодня»
    counter_completed_today = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    #раздел «В работе»
    section_in_work = (By.XPATH, ".//li[@class='text text_type_digits-default mb-2']")
