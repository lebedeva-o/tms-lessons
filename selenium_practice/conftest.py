import pytest
from selenium import webdriver

chrome_driver_path = "C:/Users/Olga/chromedriver-win64/chromedriver.exe"


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    yield driver
    driver.quit()


