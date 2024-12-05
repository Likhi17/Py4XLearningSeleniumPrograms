import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_5():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    # search_box_inout_css = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search_box_input_xpath.send_keys("macmini")

    search_box_button = driver.find_element(By.CSS_SELECTOR, "input[value='Search']")
    search_box_button.click()

    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_prize = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")



    time.sleep(5)
    driver.quit()