from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_list = driver.find_elements(By.XPATH, '//select[@id="id_choose_language"]/descendant::option[text()!=""]')
    list_language = []
    for element in choose_list:
        list_language.append(element.text)

    choose_language = driver.find_element(By.ID, 'id_choose_language')
    language_value = Select(choose_language)
    language_value.select_by_value('1')

    submit_button = driver.find_element(By.CSS_SELECTOR, '[name="submit"]')
    submit_button.click()

    result = driver.find_element(By.ID, 'result-text')
    assert result.text == list_language[0]


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button_start = driver.find_element(By.XPATH, '//div[@id="start"]/child::button')
    button_start.click()

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="finish"]/child::h4'))
    )
    assert element.text == 'Hello World!'
