import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

options.add_argument("user-data-dir=C:\\Users\\nmahesh\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("window-size=800,1000");

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\chromedriver.exe', chrome_options=options)

driver.get("https://robinhood.com/crypto/BTC")


firstDig = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[1]/section[1]/header/div[1]/h1/span/div/div[1]/span[2]"))).text

secondDig = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[1]/section[1]/header/div[1]/h1/span/div/div[1]/span[4]"))).text


thirdDig = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[1]/section[1]/header/div[1]/h1/span/div/div[1]/span[5]"))).text

fourthDig = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[1]/section[1]/header/div[1]/h1/span/div/div[1]/span[6]"))).text

decimalOne = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[1]/section[1]/header/div[1]/h1/span/div/div[1]/span[8]"))).text

decimalTwo = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div/div/div/div/div[1]/section[1]/header/div[1]/h1/span/div/div[1]/span[9]"))).text

concat = firstDig + secondDig + thirdDig + fourthDig + "." + decimalOne + decimalTwo

print(concat)

# TODO need to buy if the value drops to 6500
# Sell if the value increases to at least 7100

# while True:
#     if(float(concat) >= 6500.00):
#         print("lets gooo")