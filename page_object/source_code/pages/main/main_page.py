from page_object.source_code.pages.base_element import BaseElement
from page_object.source_code.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.card_button = BaseElement(
            driver,
            "//*[@class ='main-nav_link main-nav_link--straight' and contains(text(), 'Карты')]")

        self.red_card = BaseElement(
            driver,
            "//*[text()='Онлайн оформление карты']/..//*[@alt='Красная карта 2.0']")
