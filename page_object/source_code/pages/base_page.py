class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def hover_over(self, locator):
        pass

    def click(self, locator):
        pass

    def open_page(self, url):
        self.driver.get(url)