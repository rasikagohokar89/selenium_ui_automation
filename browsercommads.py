import time

from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

demo= driver.get_cookies()
driver.add_cookie({"name": "demo", "value": "demo"})
driver.delete_all_cookies()
print(driver.get_cookies())
# driver.minimize_window()
# driver.fullscreen_window()
# driver.get("http://saucedemo.com")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.back()
driver.refresh()
driver.close()