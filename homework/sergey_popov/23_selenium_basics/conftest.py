import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    return chrome_driver
