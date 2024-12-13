import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Select")
@allure.description("Verify Select")
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")


    select_html_tag = driver.find_element(By.ID, "dropdown")
    select = Select(select_html_tag)

    select.select_by_visible_text("Option 2")
    # Mul- Select
    select.select_by_visible_text("Option 1")
    select.select_by_index(1)

    time.sleep(5)