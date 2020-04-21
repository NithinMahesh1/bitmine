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

driver = webdriver.Remote(service.service_url)
driver.get('https://www.supremenewyork.com/')

# driver.find_elements_by_xpath('/html/body/div[2]/nav/ul/li[4]/a').click()

WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/nav/ul/li[4]/a'))).click()

WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/footer/nav/ul[2]/li[1]/a'))).click()

WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/nav/ul/li[9]/a'))).click()    

WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(text(),'Acid Yellow')]"))).click()   