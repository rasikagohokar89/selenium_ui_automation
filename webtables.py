import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://cosmocode.io/automation-practice-webtable/")

driver.execute_script("window.scrollBy(0,700)")
time.sleep(5)

table = driver.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")

print(f"No of rows: {len(rows)}")

target_value = "Algeria"

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value == cell.text:
            print(f"Found {target_value}")
            break

driver.quit()
