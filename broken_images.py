import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/broken_images")

images = driver.find_elements(By.TAG_NAME, 'img')
broken_images = []

for image in images:
    src = image.get_attribute('src')
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            print(f"The image is broken: {src}")
            broken_images.append(src)


print(f"Found {len(broken_images)} broken images")
driver.quit()