from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def test_submit_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')

    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Dart')

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Vader')

    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('dartvader@gmail.com')

    gender = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-3"]')
    gender.click()

    mobile_number = driver.find_element(By.ID, 'userNumber')
    mobile_number.send_keys('7890675534')

    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.get_attribute('22 Jun 2025')  # ----
    date_of_birth.click()

    select_month = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    month_value = Select(select_month)
    month_value.select_by_value('1')

    select_year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    year_value = Select(select_year)
    year_value.select_by_value('1987')

    day_value = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--018')
    day_value.click()

    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys('Chem')
    option_subjects = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(@class, "subjects-auto-complete") and text()="Chemistry"]')
        )
    )
    option_subjects.click()

    hobbies = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]'))
    )
    hobbies.click()

    address = driver.find_element(By.ID, 'currentAddress')
    address.send_keys('Tatuin')

    state = driver.find_element(By.ID, 'react-select-3-input')
    state.send_keys('N')
    state_option = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="state"]//div[text()="NCR"]'))
    )
    state_option.click()

    city = driver.find_element(By.ID, 'react-select-4-input')
    city.send_keys('D')
    city_option = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="city"]//div[text()="Delhi"]'))
    )
    city_option.click()

    button = driver.find_element(By.ID, 'submit')
    button.click()

    list_data = []
    data = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
    for element_tr in data:
        list_td = []
        element_value = element_tr.find_elements(By.TAG_NAME, 'td')
        for element_td in element_value:
            list_td.append(element_td.text)
        list_data.append(list_td)

    print(list_data)
