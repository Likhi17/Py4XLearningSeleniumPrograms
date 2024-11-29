from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome() # Create the Session | 62c075633fd0b0727c5c3f6eae5665ab
    driver.get("https://app.vwo.com") # Navigate to URL
    page_source_data = driver.page_source
    print(page_source_data)