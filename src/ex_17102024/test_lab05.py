import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_chorme_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,600")
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(chrome_options)  # Create the Session | 62c075633fd0b0727c5c3f6eae5665ab
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Navigate to URL
    # Chrome - incognito mode ->

    assert True == False

    # # Stop the Python int for 10 secs
    # time.sleep(10)