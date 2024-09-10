import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from utils.browser_manager import get_browser
from tests import helper
from config.config import URL

@pytest.fixture(scope="function")
def browser():
    driver = get_browser()
    yield driver
    driver.quit()

def test_order_placement(browser):
    browser.get(URL)
    home_page = HomePage(browser)
    home_page.search("C")
    WebDriverWait(browser, 10).until(
        lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".products > .product")) == 7
    )
    products = home_page.add_cart()
    names =['Brocolli - 1 Kg', 'Cucumber - 1 Kg', 'Carrot - 1 Kg', 'Corn - 1 Kg']
    helper.add_each_item_to_cart(products, names, browser)
    home_page.go_to_cart()
    home_page.proceed()
    prices = home_page.product_prices()
    helper.comapre_actual_expected_price(prices, browser)
    home_page.place_order()
    countries = home_page.select_contry(browser)
    countries.select_by_visible_text('Pakistan')
    home_page.agree()
    home_page.complete_order()
    assert "Thank you, your order has been placed successfully" in browser.page_source, "Text not found"

