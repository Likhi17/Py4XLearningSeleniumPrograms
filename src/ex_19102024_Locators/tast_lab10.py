import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Find all the buttons by TagName")
@allure.description("Verify that FREE Trail button is clicked, Navigated to next page")
def test_4():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # tag Name
    # buttons = driver.find_elements(By.TAG_NAME,"button")
    # print(len(buttons))
    # for i in buttons:
    #     print(i.text)

    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links_page))
    for i in all_links_page:
        print(i.text)






    time.sleep(5)
    driver.quit()