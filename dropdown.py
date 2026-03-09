import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
#
# dropdown_element = driver.find_element(By.ID,'dropdown')
#
# # select = Select(dropdown_element)
# # # need to get the count of options
# #
# # options_count = len(select.options)
# #
# # if options_count == 3:
# #     print('correct no of options')
#
#
#
#
# # select the value by visible text
# # select.select_by_visible_text('Option 2')
# # time.sleep(2)
# #  select the value by index
# # select.select_by_index(1)
# # time.sleep(2)
#
# # select the value by value
# # select.select_by_value('1')
# # time.sleep(2)
#
#
# # now if want to check if specific option is there then select that
# target_option = "Option 2"
#
# for option in Select(dropdown_element).options:
#     if option.text == target_option:
#         option.click()
#         break


dropdown_element = driver.find_element(By.ID, "dropdown")

select = Select(dropdown_element)

options_len = len(select.options)
assert options_len == 3

select.select_by_value("1")


select.select_by_visible_text("Option 2")
time.sleep(2)
# verify option 2 is selected

for option in select.options:
    if option.is_selected():
        assert option.text == "Option 2"
        print('passed')
        break



















