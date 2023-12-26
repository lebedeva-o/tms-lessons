from page_object.source_code.pages.base_element import BaseElement
from page_object.source_code.pages.main.main_page import MainPage


class RedCard(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.phone_number = BaseElement(
            driver,
            "//input[@type='tel']")

        self.accept_button = BaseElement(
            driver,
            "//button[contains(@class, 'submitAction')]//span[text()='Подтвердить']")