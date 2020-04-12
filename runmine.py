import selenium
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# TODO figure out how to read webpage periodically from website

# Path to the chromedriver program
service = Service('C:\Program Files (x86)\Google\chromedriver.exe')
service.start()

# Driver opens the remote with robinhood website
driver = webdriver.Remote(service.service_url)
driver.get('https://robinhood.com/crypto/BTC')

# We will grab the element id's to log on to Robinhood
# driver.find_element_by_id(“ID”).send_keys(“username”)
# driver.find_element_by_id (“ID”).send_keys(“password”)
# driver.find_element_by_id(“submit”).click()
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_3kh8OsNx6QdAbMaoKTi2Yq _1uaripz9PIQ8yApSTs6BKk']"))).click()

