import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Регистрация на сайте")
@allure.step
def test_register(browser, config):
    """
        Тест на регистрацию пользователя на сайте.

        Args:
            browser (webdriver.Chrome): WebDriver для взаимодействия с браузером.
            config (Config): Конфигурационные данные для теста.

        Assertions:
            Проверяет успешное завершение регистрации.
        """
    browser.get("https://magento.softwaretestingboard.com/")
    browser.find_element(By.LINK_TEXT, "Create an Account").click()
    browser.find_element(By.ID, "firstname").send_keys(config["firstname"])
    browser.find_element(By.ID, "lastname").send_keys(config["lastname"])
    browser.find_element(By.ID, "email_address").send_keys(config["email"])
    browser.find_element(By.ID, "password").send_keys(config["password"])
    browser.find_element(By.ID, "password-confirmation").send_keys(config["password"])
    browser.find_element(By.CSS_SELECTOR, "button[title='Create an Account']").click()
    assert "Thank you for registering with Main Website Store." in browser.page_source


@allure.title("Тестовая покупка товара")
@allure.step
def test_purchase(browser, config):
    """
        Тест на покупку товара на сайте.

        Args:
            browser (webdriver.Chrome): WebDriver для взаимодействия с браузером.
            config (Config): Конфигурационные данные для теста.

        Assertions:
            Проверяет успешное завершение покупки товара.
        """
    browser.get("https://magento.softwaretestingboard.com/")
    browser.find_element(By.LINK_TEXT, "Push It Messenger Bag").click()
    browser.find_element(By.ID, "qty").clear()
    browser.find_element(By.ID, "qty").send_keys(3)
    browser.find_element(By.CSS_SELECTOR, "button[title='Add to Cart']").click()
    browser.find_element(By.LINK_TEXT, "shopping cart").click()
    browser.find_element(By.CSS_SELECTOR, "button[data-role='proceed-to-checkout']").click()
    browser.find_element(By.NAME, "street[0]").send_keys("London St")
    browser.find_element(By.NAME, "city").send_keys("Manhattan")
    Select(browser.find_element(By.NAME, "country_id")).select_by_visible_text("China")
    Select(browser.find_element(By.NAME, "region_id")).select_by_visible_text("Henan Sheng")
    browser.find_element(By.NAME, "postcode").send_keys("123456")
    browser.find_element(By.NAME, "telephone").send_keys("88005553535")
    radio_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.radio[value="flatrate_flatrate"]')))
    radio_button.click()
    browser.find_element(By.CSS_SELECTOR, "button[data-role='opc-continue']").click()
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='Place Order']"))
    )
    # Клик с использованием JavaScript
    browser.execute_script("arguments[0].click();", button)
    WebDriverWait(browser, 10).until(EC.url_to_be("https://magento.softwaretestingboard.com/checkout/onepage/success/"))

    assert "Thank you for your purchase!" in browser.page_source

    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
