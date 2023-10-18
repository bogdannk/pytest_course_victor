from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

