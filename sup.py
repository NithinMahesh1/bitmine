import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Will eventually build this out to be more user friendly 
# Enter Keywords:
# TshirtName = input("Enter name of T-shirt: ")
# color = input("Enter color: ")

# Path to the chromedriver program
service = Service('C:\Program Files (x86)\Google\chromedriver.exe')
service.start()

driver = webdriver.Remote(service.service_url)
driver.get('https://www.supremenewyork.com/')

# driver.find_elements_by_xpath('/html/body/div[2]/nav/ul/li[4]/a').click()

WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/nav/ul/li[4]/a'))).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/footer/nav/ul[2]/li[1]/a'))).click()

WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/nav/ul/li[9]/a'))).click()    

# Need to figure out how to search by any keyword
WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, " //*[contains(text(),'Morph')] /parent::div/following-sibling::*/*[contains(text(),'Black')]"))).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='add-remove-buttons']/input"))).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/div/div[1]/div/a[2]"))).click()

# Enter name
driver.find_element_by_css_selector('#order_billing_name').send_keys("Test Testing")

# Enter Email
driver.find_element_by_css_selector('#order_email').send_keys("NithisaSav@gmail.com")

# Enter Phone
driver.find_element_by_css_selector('#order_tel').send_keys("617-111-1330")

# Enter Address
driver.find_element_by_css_selector('#bo').send_keys("25 Testing Road")

# Enter Zip
driver.find_element_by_css_selector('#order_billing_zip').send_keys("05124")

# Enter City
driver.find_element_by_css_selector('#order_billing_city').send_keys("New York")

# Enter State
driver.find_element_by_css_selector('#order_billing_state').send_keys("MA")

# Enter Credit Card Number:
driver.find_element_by_css_selector('#rnsnckrn').send_keys("41000000000000000")

# Enter Expiration Month
driver.find_element_by_css_selector('#credit_card_month').send_keys("09")

# Enter Expiration Year
driver.find_element_by_css_selector('#credit_card_year').send_keys("2019")

# Enter CVV
driver.find_element_by_css_selector('#orcer').send_keys("696")