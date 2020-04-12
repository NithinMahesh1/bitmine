import selenium
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# TODO figure out how to read webpage periodically from website

# path to the chromedriver program
service = Service('C:\Program Files (x86)\Google\chromedriver.exe')
service.start()

# driver opens the remote with robinhood website
driver = webdriver.Remote(service.service_url)
driver.get('https://robinhood.com/crypto/BTC');
time.sleep(200)

# closes the driver after timeout
driver.quit()