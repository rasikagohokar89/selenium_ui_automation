import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/')
driver.maximize_window()
time.sleep(5)


links = driver.find_elements(By.TAG_NAME,'a')
print(f"Found {len(links)} links")


for link in links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"The link {href} is broken")


driver.quit()