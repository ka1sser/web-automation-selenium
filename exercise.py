from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# webdriver object
driver = webdriver.Chrome()
driver.get("https://www.google.com")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")

for char in "tech with tim":
    search_bar.send_keys(char)
    time.sleep(random.uniform(0.5, 1))  # Random delay per keypress

search_bar.send_keys(Keys.ENTER)

time.sleep(15)

driver.quit()
