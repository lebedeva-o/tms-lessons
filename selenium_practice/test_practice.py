from selenium.webdriver.common.by import By


class TestSaurus:
    def test_search_for_synonyms(self, driver):
        driver.get("https://www.thesaurus.com/")
        search_word = driver.find_element(By.XPATH, "//*[@id='global-search']")
        search_word.send_keys("love")
        click_button = driver.find_element(By.XPATH, "//*[contains(@class, 'SFL')]")
        click_button.click()
        sixth_synonym = driver.find_element(By.XPATH, "(//*[contains(@href, 'friendship')])[1]")
        all_synonyms = driver.find_elements(By.XPATH, "(//*[contains(@data-linkid, 'y2woe7')])")
        synonym_texts = [synonym.text for synonym in all_synonyms]
        all_synonyms_text = ', '.join(synonym_texts)
        print(f'\033[1mSixth synonym word:\033[0m\n{sixth_synonym.text}')
        print(f'\033[1mAll synonyms for the word "love":\033[0m\n{all_synonyms_text}')