#Create Selenium Script
#Open the URl - https://katalon-demo-cura.herokuapp.com/
#Find and Click on the Make Appointment button
#Verify the URL
#On the Next Page
#Find and Enter the details of the username and password ( web_element.send_keys()
#Click on the Submit button (click()
#Verify the URL change.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import time

from selenium.webdriver.common.by import By


def test_katalon_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_btn = driver.find_element(By.ID,"btn-make-appointment")
    #<a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    make_appointment_btn.click()
    time.sleep(5)
    current_url = driver.current_url
    print("current_Url")
    assert current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    user_name = driver.find_element(By.ID,"txt-username")
    user_name.send_keys("John Doe")
    password = driver.find_element(By.NAME,"password")
    #<input type="password" class="form-control" id="txt-password" name="password" placeholder="Password" value="" autocomplete="off">
    password.send_keys("ThisIsNotAPassword")
    login_btn = driver.find_element(By.ID,"btn-login")
    #<button id="btn-login" type="submit" class="btn btn-default">Login</button>
    login_btn.click()
    time.sleep(5)
    assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/#appointment"
    print(driver.current_url)
    time.sleep(5)