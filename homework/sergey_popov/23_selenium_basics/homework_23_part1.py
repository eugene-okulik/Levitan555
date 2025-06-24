from selenium.webdriver.common.by import By


def test_submit_text(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    some_text = driver.find_element(By.ID, 'id_text_string')
    some_text.send_keys('Hello')
    some_text.submit()
    text_result = driver.find_element(By.ID, 'result-text')
    print(text_result.text)
