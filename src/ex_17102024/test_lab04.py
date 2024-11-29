from selenium import webdriver


def test_task2():
    driver = webdriver.Chrome()  # Create the Session | 62c075633fd0b0727c5c3f6eae5665ab
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Navigate to URL
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()

