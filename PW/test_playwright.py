# 1. Открыть сайт https://blizko.by/
# 2. Перейти на страницу "Каталог"
# 3. Развернуть выпадашку "Дом"
# 4. Выбрать "Товары для дома"
# 5. Нажать на кнопку "Телефоны" у первого мазагазина
# Ожидаемый результат
# На появившейся модалке есть заголовок, адрес, несколько телефонов, кнопка закрытия и фраза "Пожалуйста, сообщите администратору, что нашли этот телефон на Blizko.by" в футере
# === Со звездочкой ===
# - проверить, что заголовок жирный (только не говорите ему :) )
# - проверить, что телефон в формате 8(ХХХ) ХХХ-ХХ-ХХ
# - проверить, что телефон - это не просто текст
from playwright.sync_api import expect


class TestPW:
    def test_cats(self, page):
        page.goto("https://blizko.by/")
        page.wait_for_load_state()
        page.get_by_role("link", name="Каталог").click()
        page.wait_for_url("**/companies")
        page.get_by_text("Дом", exact=True).click()
        page.get_by_role("link", name="Товары для дома").click()
        page.get_by_role("link", name="Телефоны").first.click()

        modal_title = page.locator("//*[@id='modalSet']//div[@class='ttl']")
        address = page.locator("//*[@id='modalSet']//div[@class='descr']")
        expect(address).to_be_visible()
        title_font_weight_actual = int(modal_title.evaluate(
            "(e) => {return"
            " window.getComputedStyle(e).getPropertyValue('font-weight');"
            "}"))
        assert title_font_weight_actual >= 700, "Стиль шрифта не жирный"


        expect(page.get_by_role("link", name="(017) 270-60-12")).to_be_visible()
        expect(page.get_by_role("link", name="(029) 619-43-16")).to_be_visible()
        expect(page.get_by_role("link", name="(029) 123-88-33")).to_be_visible()
        expect(page.locator("#modalSet")).to_contain_text(
            "Пожалуйста, сообщите администратору, что нашли этот телефон на Blizko.by")
        close_button = page.get_by_role("link", name="×")
        expect(close_button).to_be_visible()
        expect(close_button).to_be_enabled()
