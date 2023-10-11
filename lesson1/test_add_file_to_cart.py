from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_item_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    title_before = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class = 'inventory_item_name'] ").text

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[data-test = 'add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()

    cart = driver.find_element(By.CSS_SELECTOR, "a[class = 'shopping_cart_link']")
    cart.click()

    title_after = driver.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link'] > div[class = 'inventory_item_name'] ").text

    assert title_before == title_after, "Текст не совпадает"
    time.sleep(5)


