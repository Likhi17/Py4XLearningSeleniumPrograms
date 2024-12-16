import allure
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


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_action_makemytrip():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")


    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    # //span[@data-cy="closeModal"] wait -> click
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
    )

    driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()

    time.sleep(2)

    fromCity = driver.find_element(By.ID, "fromCity")
    # fromCity = driver.find_element(By.XPATH, "//input[@id='fromCity']")

    # move the mouse to fromCity - Input Box
    # click on it
    # DEL enter
    # Arrow - first ( up and down)
    # Enter

    actions = ActionChains(driver)
    (actions.
     move_to_element(fromCity)
     .click().send_keys("del")
     .perform())

    time.sleep(5)

    actions.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()


    time.sleep(10)
    driver.quit()