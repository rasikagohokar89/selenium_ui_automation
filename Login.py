from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.Chrome()
driver.get("http://saucedemo.com")
driver.maximize_window()


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

assert not driver.find_element(By.ID, "login-button").get_attribute("disabled")
driver.find_element(By.ID, "login-button").click()

products_page = driver.find_element(By.CSS_SELECTOR, "#header_container > div.header_secondary_container > span")
products_page.is_displayed()

assert  products_page.text == "Products"


