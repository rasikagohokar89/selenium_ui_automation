import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")
time.sleep(5)


actions = ActionChains(driver)
elemnent = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/a')
actions.move_to_element(elemnent).perform()

driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[3]/a').click()
time.sleep(5)

driver.quit()