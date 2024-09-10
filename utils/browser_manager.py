# utils/browser_manager.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
