import pytest
from selenium import webdriver

from page_object.source_code.pages.main.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver


@pytest.fixture(autouse=True)
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.driver.get("https://myfin.by")
