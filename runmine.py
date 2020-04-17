import selenium
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Grab user log in credentials
username = input("Enter Username ")
password = input("Enter Password ")

# Path to the chromedriver program
service = Service('C:\Program Files (x86)\Google\chromedriver.exe')
service.start()

# Driver opens the remote with robinhood website
driver = webdriver.Remote(service.service_url)
driver.get('https://robinhood.com/crypto/BTC')

# We will grab the element id's to log on to Robinhood
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "//span[contains(text(),'Log In')]"))).click()

driver.find_element_by_css_selector(
    'div.form-group:nth-child(1) > label:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(
    username)

driver.find_element_by_css_selector(
    'div.form-group:nth-child(2) > label:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(
    password)

driver.find_element_by_css_selector(
    'div.form-group:nth-child(2) > label:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(Keys.ENTER)

# driver.find_elements_by_class_name('_3kh8OsNx6QdAbMaoKTi2Yq hJ4K1g8Iw9BKNXpQ6RnRQ').click()

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, '_3kh8OsNx6QdAbMaoKTi2Yq hJ4K1g8Iw9BKNXpQ6RnRQ')).click()
