import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Find all the buttons by TagName")
@allure.description("Verify that FREE Trail button is clicked, Navigated to next page")
def test_5():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_input_tag = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
    first_name_input_tag.send_keys("Hello")





    time.sleep(5)
    driver.quit()