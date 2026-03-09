import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Iframe is html iside html , so for this need to switch to iframes eg text editor



driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(5)

iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

text_editor = driver.find_element(By.ID, "tinymce")
text_editor.clear()
text_editor.send_keys("Hello Rasika , you are going to shine")

driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR,'#page-footer > div > div > a').click()

time.sleep(5)

driver.quit()