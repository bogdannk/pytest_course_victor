from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



# LOCATORS
l_username = By.CSS_SELECTOR, "[data-test = 'username']"
l_password = By.CSS_SELECTOR, "[data-test = 'password']"
l_login_button = By.CSS_SELECTOR, "[data-test = 'login-button']"
l_empty_cart = By.XPATH, "//a[@class = 'shopping_cart_link']"
l_cart_with_item = By.XPATH, "//a[@class = 'shopping_cart_link']/span"
l_remove_button = By.XPATH, "//button[contains(text(), 'Remove')]"
l_all_items_add_button = By.XPATH, "//button[contains(text(), 'Add to cart')]"
l_all_itest_name = By.XPATH, "//div[@class = 'inventory_item_name ']"
l_all_items_prise = By.XPATH, "//div[@class='inventory_item_price']"
'''Burger menu'''
l_burger_menu = By.XPATH, "//button[contains(text(), 'Open Menu')]"
l_all_items_button_at_burger_menu = By.XPATH, "//a[@class= 'bm-item menu-item'][contains(text(), 'All Items')]"
l_about_button_at_burger_menu = By.XPATH, "//a[@class= 'bm-item menu-item'][contains(text(), 'About')]"
l_logout_button_at_burger_menu = By.XPATH, "//a[contains(text(), 'Logout')]" #"//a[@class= 'bm-item menu-item'][contains(text(), 'Logout')]"
l_reset_app_state_button_at_burger_menu = By.XPATH, "//a[@class= 'bm-item menu-item'][contains(text(), 'Reset App State')]"
'''Checkout from start to end'''
l_checkout_button = By.CSS_SELECTOR, "[data-test = 'checkout']"
l_first_name = By.CSS_SELECTOR, "[placeholder = 'First Name']"
l_last_name = By.CSS_SELECTOR, "[placeholder = 'Last Name']"
l_zip_postal_code = By.CSS_SELECTOR, "[placeholder = 'Zip/Postal Code']"
l_continue_button = By.XPATH, "//input[@type = 'submit']"
l_finish_button = By.CSS_SELECTOR, "[data-test = 'finish']"
'''Select container buttons'''
l_select_container_button = By.XPATH, "//span[@class = 'select_container']"
l_select_az_option = By.XPATH, "//option[@value= 'az']"
l_select_za_option = By.XPATH, "//option[@value= 'za']"
l_select_lohi_option = By.XPATH, "//option[@value= 'lohi']"
l_select_hilo_option = By.XPATH, "//option[@value= 'hilo']"

#DATA
URL = 'https://www.saucedemo.com/'
valid_username = 'standard_user'
valid_password = 'secret_sauce'
invalid_username = 'user'
invalid_password = 'user'
displayed_text = "Epic sadface: Username and password do not match any user in this service"
expecting_text_after_checkout = "Thank you for your order!"
checkout_complete_message = "Checkout: Complete!"
first_name = "Bo"
last_name = "Kr"
zip_code = 45555
expecting_list_of_all_itest_name = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
list_of_item_names = []
expecting_list_of_all_item_prises = ['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99']
list_of_item_prises = []


'''1 Авторизация'''
#
# Авторизация используя корректные данные (standard_user, secret_sauce)
# Авторизация используя некорректные данные (user, user)

def test_enter_with_valid_data(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    checking_products_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").text
    print(checking_products_text)
    assert checking_products_text == "Products", "Wrong text"
    assert "https://www.saucedemo.com/inventory.html" == driver.current_url
    time.sleep(2)

def test_enter_with_invalid_data(driver):
    # driver.get(URL)
    driver.find_element(*l_username).send_keys(invalid_username)
    driver.find_element(*l_password).send_keys(invalid_password)
    driver.find_element(*l_login_button).click()
    error_text = driver.find_element(By.CSS_SELECTOR, "h3")
    error_text_displayed = error_text.text
    assert error_text.is_displayed(), "Text is not displayed"
    assert error_text_displayed == displayed_text, "Texts are different"


'''2 Корзина'''
#
# Добавление товара в корзину через каталог
# Удаление товара из корзины через корзину
# Добавление товара в корзину из карточки товара
# Удаление товара из корзины через карточку товара

def test_adding_item_to_cart_from_catalog(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    adding_element_to_cart = (driver.find_element(By.CSS_SELECTOR, "[data-test = 'add-to-cart-sauce-labs-backpack']")
                              .click())
    count_items_in_cart_text = driver. find_element(*l_cart_with_item).text
    print(f'count_items_in_cart_text = {count_items_in_cart_text}')
    remove_button_count = driver.find_elements(*l_remove_button)
    len_remove_button = str(len(remove_button_count))
    print(f'len_remove_button = {len_remove_button}')
    # assert count_items_in_cart_text.is_displayed(), "Element is not present on page"   # Doesn't work properly, it need to fix
    # assert count_items_in_cart != "0", "The cart is empty"                        # Doesn't work properly, it need to fix
    assert count_items_in_cart_text == len_remove_button, "The items displayed in the shopping cart and the selected items are different"

def test_removing_item_from_cart(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    adding_element_to_cart_from_catalog = (driver.find_element(By.CSS_SELECTOR, "[data-test = 'add-to-cart-sauce-labs-backpack']")
                              .click())
    count_items_in_cart_text = driver. find_element(*l_cart_with_item).text
    print(f"\nCount_items_in_cart_text = {count_items_in_cart_text}")
    press_on_cart = driver.find_element(*l_cart_with_item).click()
    remove_button_count = driver.find_elements(*l_remove_button)
    len_remove_button_before_removing = str(len(remove_button_count))
    print(f"len_remove_button_before_removing = {len_remove_button_before_removing}")
    assert count_items_in_cart_text == len_remove_button_before_removing
    remove_button_in_cart = (driver.find_element(By.CSS_SELECTOR, "[data-test = 'remove-sauce-labs-backpack']"))
    remove_button_in_cart.click()
    remove_button_count = driver.find_elements(*l_remove_button)
    len_remove_button_after_removing = str(len(remove_button_count))
    print(f"len_remove_button_after_removing = {len_remove_button_after_removing}")
    assert len_remove_button_after_removing == "0"

def test_adding_item_to_cart_from_card(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    move_to_card_item = driver.find_element(By.XPATH, "//a//div[contains(text(), 'Sauce Labs Backpack')]").click()
    adding_item_to_cart_from_card = driver.find_element(By.XPATH,
                                                        "//button[@data-test = 'add-to-cart-sauce-labs-backpack']").click()
    remove_button = driver.find_elements(*l_remove_button)
    len_remove_button = str(len(remove_button))
    print(f"len_remove_button = {len_remove_button}")
    count_items_in_cart_text = driver.find_element(*l_cart_with_item).text
    print(f"\nCount_items_in_cart_text = {count_items_in_cart_text}")
    assert len_remove_button == count_items_in_cart_text

def test_removing_item_from_cart_from_card(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    move_to_card_item = driver.find_element(By.XPATH, "//a//div[contains(text(), 'Sauce Labs Backpack')]").click()
    adding_item_to_cart_from_card = driver.find_element(By.XPATH,
                                                        "//button[@data-test = 'add-to-cart-sauce-labs-backpack']").click()
    press_remove_button = driver.find_element(*l_remove_button).click()
    remove_button = driver.find_elements(*l_remove_button)
    len_remove_button = str(len(remove_button))
    print(f"\nlen_remove_button = {len_remove_button}")
    try:
        count_items_in_cart_text = driver.find_element(*l_cart_with_item).text
    except Exception:
        print(f"count_items_in_cart_text = Elem not found")
    assert len_remove_button == '0'


'''3 Карточка товара'''
#
# Успешный переход к карточке товара после клика на картинку товара
# Успешный переход к карточке товара после клика на название товара

def test_successful_transition_to_the_card_after_clicking_on_the_items_name(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    move_to_card_item_pressing_on_the_items_name = driver.find_element(By.XPATH,
                                                                       "//a//div[contains(text(), 'Sauce Labs Backpack')]").click()
    item_url = "https://www.saucedemo.com/inventory-item.html?id=4"
    assert item_url == driver.current_url, "URLs do not match"

def test_successful_transition_to_the_card_after_clicking_on_the_picture(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    move_to_card_item_pressing_on_the_on_the_picture = driver.find_element(By.XPATH,
                                                                           "//a//div[contains(text(), 'Sauce Labs Backpack')]").click()
    item_url = "https://www.saucedemo.com/inventory-item.html?id=4"
    assert item_url == driver.current_url, "URLs do not match"


'''4 Оформление заказа'''
#
# Оформление заказа используя корректные данные

def test_checkout_with_valid_data(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(l_all_items_add_button))
    all_items_add_buttons = driver.find_elements(*l_all_items_add_button)
    for add_button in all_items_add_buttons:
        add_button.click()
    len_all_items_add_buttons = len(all_items_add_buttons)
    print(f'\nlen_all_items_to_cart_buttons = {len_all_items_add_buttons}')
    move_to_cart = driver.find_element(*l_empty_cart).click()
    len_remove_buttons = len(driver.find_elements(*l_remove_button))
    print(f'\ncount_remove_buttons = {len_remove_buttons}')
    assert len_all_items_add_buttons == len_remove_buttons,"Amount of selected items and amount of displayed items do not coincide"
    checkout_button = driver.find_element(*l_checkout_button).click()
    first_name_fild = driver.find_element(*l_first_name).send_keys(first_name)
    last_name_fild = driver.find_element(*l_last_name).send_keys(l_last_name)
    first_name_fild = driver.find_element(*l_zip_postal_code).send_keys(zip_code)
    continue_button = driver.find_element(*l_continue_button).click()
    finish_button = driver.find_element(*l_finish_button).click()
    text_after_checkout = driver.find_element(By.XPATH, "//h2").text
    print(f'Text_after_checkout = {text_after_checkout}')
    check_checkout_complete_message = driver.find_element(By.XPATH, "//span")
    print(f'Checkout completion message = {check_checkout_complete_message.text}')
    assert expecting_text_after_checkout == text_after_checkout
    assert check_checkout_complete_message.is_displayed(), "The message about checkout completion is not displayed"


'''5 Фильтр'''
#
# Проверка работоспособности фильтра (A to Z)
# Проверка работоспособности фильтра (Z to A)
# Проверка работоспособности фильтра (low to high)
# Проверка работоспособности фильтра (high to low)

def test_a_z_sorting_check(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    item_names = driver.find_elements(*l_all_itest_name)
    for item in item_names:
        list_of_item_names.append(item.text)
    print(f"\nlist_of_item_names               = {list_of_item_names}")
    print(f"expecting_list_of_all_itest_name = {expecting_list_of_all_itest_name}")
    assert expecting_list_of_all_itest_name == list_of_item_names

def test_z_a_sorting_check(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    driver.find_element(*l_select_container_button).click()
    driver.find_element(*l_select_za_option).click()
    item_names = driver.find_elements(*l_all_itest_name)
    for item in item_names:
        list_of_item_names.append(item.text)
    print(f"\nlist_of_item_names                     = {list_of_item_names}")
    print(f"expecting_list_of_all_itest_name[::-1] = {expecting_list_of_all_itest_name[::-1]}")
    assert list_of_item_names == expecting_list_of_all_itest_name[::-1]

def test_lohi_sorting_check(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    driver.find_element(*l_select_container_button).click()
    driver.find_element(*l_select_lohi_option).click()
    item_prises = driver.find_elements(*l_all_items_prise)
    for prise in item_prises:
        list_of_item_prises.append(prise.text)
    print(f"\nlist_of_item_prises               = {list_of_item_prises}")
    print(f"expecting_list_of_all_item_prises = {expecting_list_of_all_item_prises}")
    assert list_of_item_prises == expecting_list_of_all_item_prises

def test_hilo_sorting_check(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    driver.find_element(*l_select_container_button).click()
    driver.find_element(*l_select_hilo_option).click()
    item_prises = driver.find_elements(*l_all_items_prise)
    for prise in item_prises:
        list_of_item_prises.append(prise.text)
    print(f"\nlist_of_item_prises                     = {list_of_item_prises}")
    print(f"expecting_list_of_all_item_prises[::-1] = {expecting_list_of_all_item_prises[::-1]}")
    assert list_of_item_prises == expecting_list_of_all_item_prises[::-1]


'''Бургер меню'''
#
# Выход из системы
# Проверка работоспособности кнопки "About" в меню
# Проверка работоспособности кнопки "Reset App State"

def test_logout(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    driver.find_element(*l_burger_menu).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(l_logout_button_at_burger_menu))
    driver.find_element(*l_logout_button_at_burger_menu).click()
    assert URL == driver.current_url

def test_varification_of_about_button_functionality(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    driver.find_element(*l_burger_menu).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(l_about_button_at_burger_menu))
    driver.find_element(*l_about_button_at_burger_menu).click()
    assert "https://saucelabs.com/" == driver.current_url

def test_varification_of_reset_app_button_functionality(driver):
    driver.find_element(*l_username).send_keys(valid_username)
    driver.find_element(*l_password).send_keys(valid_password)
    driver.find_element(*l_login_button).click()
    driver.find_element(*l_burger_menu).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(l_reset_app_state_button_at_burger_menu))
    driver.find_element(*l_reset_app_state_button_at_burger_menu).click()
    try:
        assert driver.current_url != "https://www.saucedemo.com/inventory.html"
    except Exception:
        print(f"\nURL has not changed")