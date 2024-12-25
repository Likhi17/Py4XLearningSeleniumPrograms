import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


class TestSelenium():
    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.maximize_window()

    @pytest.mark.smoke
    def test_js(self):
        title = self.driver.execute_script("return document.title")
        current_url = self.driver.execute_script("return document.URL")
        print(current_url)
        print(title)
        assert current_url == "https://selectorshub.com/xpath-practice-page/"

    def close_browser(self):
        time.sleep(3)  # Wait for 3 seconds before closing
        self.driver.quit()


test = TestSelenium()
test.open_browser()
test.test_js()
test.close_browser()


# import allure
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
# @pytest.fixture(scope="class")
# def setup_class(request):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--incognito")
#     driver = webdriver.Chrome(chrome_options)
#     driver.get("https://selectorshub.com/xpath-practice-page/")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     time.sleep(3)  # Wait for 3 seconds before closing
#     driver.quit()
#
# @pytest.mark.usefixtures("setup_class")
# class TestSelenium:
#     def test_js(self):
#         title = self.driver.execute_script("return document.title")
#         current_url = self.driver.execute_script("return document.URL")
#         print(current_url)
#         print(title)
#         assert current_url == "https://selectorshub.com/xpath-practice-page/"

