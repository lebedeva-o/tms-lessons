import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def assert_element(driver, xpath_value, clickable=False, wait_timeout=10):
    xpath = (By.XPATH, xpath_value)
    wait = WebDriverWait(driver, wait_timeout)
    wait.until(EC.presence_of_element_located(xpath))
    wait.until(EC.visibility_of_element_located(xpath))

    if clickable:
        wait.until(EC.element_to_be_clickable(xpath))

    result = driver.find_element(*xpath)
    return result


# def click(driver, xpath):
#     element = assert_element(driver, xpath, clickable=True)
#     element.click()

#
# class TestMyfin:
#     def test_my_fin(self, driver):
#         driver.get("https://myfin.by")
#         actions = ActionChains(driver)
#         cards = assert_element(driver, "//a[@href='/cards']")
#         actions.move_to_element(cards).perform()
#         click(driver, "//*[text()='Онлайн оформление карты']/..//*[@alt='Красная карта 2.0']")
#
#         driver.switch_to.window(driver.window_handles[-1])
#
#         phone_number = assert_element(driver, "//input[@type='tel']")
#         phone_number.send_keys("299402265")
#
#         click(driver, "//button[contains(@class, 'submitAction')]//span[text()='Подтвердить']")
#
#         for _ in range(10):
#             autentificate = assert_element(driver, "//*[@class='title']")
#             autentificate_text = autentificate.get_attribute("textContent")
#             if autentificate_text == "Пройдите идентификацию":
#                 break
#             time.sleep(1)
#         else:
#             raise Exception("Different kind of text")
#
#         msi_botton = assert_element(driver, "//*[@class='title']")
#         button_style = msi_botton.value_of_css_property("background-color")
#         assert msi_botton.is_displayed()
#         assert button_style