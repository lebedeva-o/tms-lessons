from page_object.source_code.pages.cards.red_card_2 import RedCard
from page_object.source_code.pages.main.main_page import MainPage


class TestClass:
    def test_card_button(self, driver):
        main_page = MainPage(driver)

        main_page.card_button.hover()
        main_page.red_card.click()

        driver.switch_to.window(driver.window_handles[-1])

        red_card = RedCard(driver)
        red_card.phone_number.send_keys("299402265")

        red_card.accept_button.click()
