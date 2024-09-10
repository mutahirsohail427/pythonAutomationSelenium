# conftest.py
import pytest
from utils.browser_manager import get_browser

@pytest.fixture(scope="session")
def browser():
    driver = get_browser()
    yield driver
    # driver.quit()
