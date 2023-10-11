from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_logout():
    driver.get("https://www.saucedemo.com/")

    start_url = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Open Menu')]").click()
    time.sleep(1)

    logout_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()

    # text_presents = driver.find_element(By.XPATH, "//div[contains(text(), 'Swag Labs')]")

    end_url = driver.current_url

    assert start_url == end_url

