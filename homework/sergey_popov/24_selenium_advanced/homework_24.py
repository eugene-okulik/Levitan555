from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test_first(driver):
    driver.get('https://www.demoblaze.com/index.html')

    product = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//a[@href="prod.html?idp_=1" and @class="hrefch"]'))
    )
    product_text = product.text
    ActionChains(driver).key_down(Keys.COMMAND).click(product).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[1])

    add_cart = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[onclick="addToCart(1)"]'))
    )
    add_cart.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    cart = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'cartur'))
    )
    ActionChains(driver).key_down(Keys.COMMAND).click(cart).key_up(Keys.COMMAND).perform()

    driver.switch_to.window(driver.window_handles[1])
    prod_in_cart = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.success td:nth-child(2)'))
    )
    assert prod_in_cart.text == product_text


def test_second(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'fc-button-label'))).click()

    element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//li[@class="item product product-item"][1]//a[@class="product-item-link"]')
        )
    )
    element_text = element.text.strip()
    ActionChains(driver).move_to_element(element).perform()

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//li[@class="item product product-item"][1]//a[@class="action tocompare"]')
        )
    ).click()

    element_to_compare = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//li[@class="product-item odd last"]//a[@class="product-item-link"]')
        )
    )
    assert element_to_compare.text == element_text
