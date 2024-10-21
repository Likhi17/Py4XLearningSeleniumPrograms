from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome()
    #  POST request to create a New FRESH copy of Chrome
    #  Fresh - Chrome - Session ID - 6e31bb70-4809-4b20-8d87-cce289af6ce1


    driver.get("https://app.vwo.com")
    # Code -> HTTP Request -. ChromeDriver(Selenium Manager) -> chROME (SessionID)

    print(driver.title) # GET Request t
    assert driver.title == "Login - VWO"