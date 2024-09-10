from pages.home_page import HomePage

def add_each_item_to_cart(products, names, browser):
    home_page = HomePage(browser)
    for product in products:
        name_element = home_page.get_products_name(product)
        product_name = name_element.text
        if product_name in names:
            add_cart_button = home_page.add_to_cart(product)
            add_cart_button.click()

def comapre_actual_expected_price(prices, browser):
    home_page = HomePage(browser)
    sum_of_all_items = 0
    for price in prices:
        sum_of_all_items = sum_of_all_items + int(price.text)
    print(sum_of_all_items)
    total_amount = home_page.total_of_products()
    assert sum_of_all_items == int(total_amount), f"Expected {sum_of_all_items}, but got {int(total_amount)}"