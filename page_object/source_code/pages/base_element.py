from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BaseElement:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath

    def hover(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.xpath)
        actions.move_to_element(element).perform()

    def click(self):
        pass

    def send_keys(self, text):
        element = self.driver.find_element(self.xpath)
        element.send_keys(text)
