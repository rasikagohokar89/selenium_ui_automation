# So you have to go inside the frames to access and then to switch frames , first move to default_content and then again switch to another frame


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")


top_frame = driver.find_element(By.XPATH, "/html/frameset/frame[1]")
driver.switch_to.frame(top_frame)

middle_frame = driver.find_element(By.XPATH, "/html/frameset/frame[2]")
driver.switch_to.frame(middle_frame)

middle_frame_content = driver.find_element(By.ID, "content")
print(middle_frame_content.text)

driver.switch_to.default_content()

bottom_frame = driver.find_element(By.XPATH, "/html/frameset/frame[2]")
driver.switch_to.frame(bottom_frame)

body = driver.find_element(By.XPATH, "/html/body")
print(body.text)

