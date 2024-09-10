from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SEARCH_BOX = (By.CLASS_NAME, 'search-keyword')
    PRODUCTS = (By.CSS_SELECTOR, '.products > .product')
    CART_ICON = (By.CSS_SELECTOR, '.cart-icon > img')
    PROCEED = (By.CSS_SELECTOR, '.cart-preview > .action-block > button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'tr td:nth-child(4)')
    TOTAL_AMT = (By.CSS_SELECTOR, '.totAmt')
    PLACE_ORDER = (By.CSS_SELECTOR, 'div > button:not(.promoBtn)')
    SELECT_COUNTRY = (By.CSS_SELECTOR, "select")
    AGREE = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    COMPLETE = (By.CSS_SELECTOR, 'div > button')

    def search(self, text):
        self.enter_text(self.SEARCH_BOX, text)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def proceed(self):
        self.click(self.PROCEED)

    def add_cart(self):
        return self.get_item_list(self.PRODUCTS)

    def get_products_name(self, product):
        return product.find_element(By.CLASS_NAME, 'product-name')

    def add_to_cart(self, product):
        return product.find_element(By.CSS_SELECTOR, '.product-action > button[type="button"]')

    def product_prices(self):
        return self.get_multi_text(self.PRODUCT_PRICE)[1:]

    def total_of_products(self):
        return self.get_text(self.TOTAL_AMT)

    def place_order(self):
        return self.click(self.PLACE_ORDER)

    def select_contry(self, browser):
        return Select(browser.find_element(By.CSS_SELECTOR, "select"))

    def agree(self):
        return self.click(self.AGREE)

    def complete_order(self):
        return self.click(self.COMPLETE)

