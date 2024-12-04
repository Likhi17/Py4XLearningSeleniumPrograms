import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Positive Testcase - App.vwo.com Singup Button Verification. ")
@allure.description("Verify that FREE Trail button is clicked, Navigated to next page")
def test_negative_vwo_free_trail_project3():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    #<a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # LINK_TEXT = EXACT Match
    # anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    # anchor_tag_element.click()

    # PARTIAL_LINK_TEXT - contains
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    anchor_tag_element.click()




    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    driver.back()






    time.sleep(5)
    driver.quit()