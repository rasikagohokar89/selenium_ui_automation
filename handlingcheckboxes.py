import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
time.sleep(5)


# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
print(checkboxes)
for checkbox in checkboxes:
    checkbox.click()
    print(checkbox.get_attribute('checked'))

expected = 1
count = 0
for checkbox in checkboxes:
    if checkbox.get_attribute('checked') == "true":
        count += 1

assert count == expected

for checkbox in checkboxes:
    assert checkbox.is_selected()
    print(checkbox.is_selected())




time.sleep(5)