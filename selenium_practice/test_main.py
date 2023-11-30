import pytest
import random


class TestWebsites:

    @pytest.mark.parametrize("url", ["https://www.amazon.com//",
                                     "https://www.apple.com/",
                                     "https://www.google.com/"])
    @pytest.mark.parametrize("page_title", ["Amazon.com",
                                            "Apple",
                                            "Google"])
    def test_open_sites(self, url, page_title, driver):
        driver.get(url)
        screenshot_path = (f"D:/O/tms_lessons/selenium_practice/screenshots/{random.randint(1, 100)}.jpg")
        driver.save_screenshot(screenshot_path)
        actual_title = driver.title
        assert actual_title == page_title
