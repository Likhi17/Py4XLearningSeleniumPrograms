import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG")
@allure.description("Verify svg")
def test_verify_svg():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    element = driver.find_element(By.ID, "this_id_doesnt_exist")
    # response =
    # {'status': 404, 'value': '
    # {"value":{"error":"no such element","message":
    # "no such element: Unable to locate element:

    # NoSuchElementException


    time.sleep(5)