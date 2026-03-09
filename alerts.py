import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# # the alerts cannot be inpected as they do not have locators
# #   Alert variation 1
# alert_1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
# alert_1.click()

# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()

# # alert variation 2
# alert_2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
# alert_2.click()

# alert = driver.switch_to.alert
# print(alert.text)

# alert.dismiss()

# alert variation 3
alert_3 = driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button')
alert_3.click()

alert = driver.switch_to.alert
time.sleep(5)
alert.send_keys('wejbfewuj')
alert.accept()
