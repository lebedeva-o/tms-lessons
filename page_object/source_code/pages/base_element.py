from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath

    def find_element(self, xpath):
        ec = expected_conditions
        xpath_locator = (By.XPATH, xpath)
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(ec.presence_of_element_located(xpath_locator))
        wait.until(ec.visibility_of_element_located(xpath_locator))
        wait.until(ec.element_to_be_clickable(xpath_locator))

        return element

    def hover(self):
        actions = ActionChains(self.driver)
        element = self.find_element(self.xpath)
        actions.move_to_element(element).perform()

    def click(self):
        element = self.find_element(self.xpath)
        element.click()

    def send_keys(self, text):
        element = self.find_element(self.xpath)
        element.send_keys(text)