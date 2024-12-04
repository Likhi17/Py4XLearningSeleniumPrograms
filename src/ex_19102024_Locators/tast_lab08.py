import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@pytest.mark.negative
@allure.title("Negative Testcase - App.vwo.com - Wrong Email, Pass -> Error Message.")
@allure.description("Verify that if email/pass is wrong, we will get a message")
def test_negative_vwo_login_project2():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")


    # Find the email,
    # Find the password,

    #<input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # data-gtm-form-interact-field-id="1">

    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys("password@1234")

    # Click on the Sign Button

    # <button type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica"
    # >

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    # Wait for sometime
    time.sleep(3)



    # Verify that message is visible.
    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match</div>

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"


    time.sleep(5)
    driver.quit()