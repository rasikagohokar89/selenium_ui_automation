import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.switch_to.new_window("window")
driver.get("https://playwright.dev")
time.sleep(5)
number_tabs = len(driver.window_handles)
print(f"Found {number_tabs} tabs")

tab_value = driver.window_handles
print(tab_value)

current_tab = driver.current_window_handle
print(current_tab)

driver.find_element(By.CLASS_NAME, "getStarted_Sjon").click()
time.sleep(5)

driver.switch_to.window(tab_value[0])

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div/footer/div/div/div[3]/p/a').click()
time.sleep(5)