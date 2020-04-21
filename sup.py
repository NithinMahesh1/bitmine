import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Path to the chromedriver program
service = Service('C:\Program Files (x86)\Google\chromedriver.exe')
service.start()

# Driver opens the remote with robinhood website
driver = webdriver.Remote(service.service_url)
driver.get('https://www.supremenewyork.com/')

# We will grab the element id's to log on to Robinhood
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/nav/ul/li[4]/a'))).click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/footer/nav/ul[2]/li[1]/a'))).click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/nav/ul/li[9]/a'))).click()    