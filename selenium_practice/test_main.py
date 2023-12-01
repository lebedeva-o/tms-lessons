import pytest
import random


class TestWebsites:

    @pytest.mark.parametrize("url, page_title",
                             [
                                 ("https://www.amazon.com//", "Amazon.com"),
                                 ("https://www.apple.com/", "Apple"),
                                 ("https://www.google.com/", "Google")
                             ],
                             )
    def test_open_sites(self, url, page_title, driver):
        driver.get(url)
        screenshot_path = (f"D:/O/tms_lessons/selenium_practice/screenshots/{random.randint(1, 100)}.png")
        driver.save_screenshot(screenshot_path)
        actual_title = driver.title
        assert actual_title == page_title


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call' and rep.failed:
#         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         driver = item.funcargs['driver']
#         driver.save_screenshot(f"fail_{now}.png")
#
# //*[@id='gh-ac']
#
# //*[contains(@href, '/company')]
# a[href*='/company']
# //*[contains(text(), 'Сведения')]

# def click(driver, xpath_value):
#     xpath = (By.XPATH, xpath_value)
#     wait = WebDriverWait(driver, 10)
#     for condition in [
#         EC.presence_of_element_located,
#         EC.visibility_of_element_located,
#         EC.element_to_be_clickable,
#     ]:
#         wait.until(condition(xpath))
#     element = driver.find_element(*xpath)
#     element.click()