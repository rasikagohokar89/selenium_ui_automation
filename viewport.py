import time

from selenium import webdriver


viewports = [(786,1024),(1024,786)]


driver = webdriver.Chrome()
driver.get("https://www.google.com")


try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(5)

finally:
    driver.close()
