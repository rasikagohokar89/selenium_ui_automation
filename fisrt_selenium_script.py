import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com")
driver.maximize_window()

# also once we land a page we can do verifications for tittle or current_url
current_title = driver.title
print(current_title)
expected_title = 'Demo eCom Store – Shop Till You Drop!!'

if expected_title != current_title:
    raise Exception("Expected title to be '" + expected_title + "', but got '" + current_title + "'")
#
# # Search element by ID
# cart = driver.find_element(By.ID,"site-header-cart")
# print(cart.text)
#
# # Use keys
# # difference between find_element and find_elements is that you get a list in case of elements and otherwise a single element
# search_field = driver.find_element(By.ID,"woocommerce-product-search-field-0")
# search_field.send_keys("Hoodie")
# search_field.send_keys(Keys.ENTER)
#
# #pdb.set_trace() # the execution stops here and you can run commands like dir(driver) or any command
#
# # driver.implicitly_wait(10) -->wait until the element is visible
#
# # Search by xpath
# account = driver.find_element(By.XPATH,'//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
# account.click()
#
# # Also you can check if element is displayed once you click on something below is the example
# if account.is_displayed():
#     print(account.text)
# else:
#     raise Exception("Account is not displayed")


# # Test flow -> add item to cart , apply invalid coupon and verify the alert message
#
# select_item_xpath = '//*[@id="main"]/ul/li[1]/a[2]'
# driver.find_element(By.XPATH, select_item_xpath).click()
# driver.implicitly_wait(10)
# # View the cart
# driver.find_element(By.XPATH,'//*[@id="main"]/ul/li[1]/a[3]').click()
#
# # Verify the product added to cart
# product_xpath = '//*[@id="post-7"]/div/div/div[4]/div/div/div[2]/table/tbody/tr/td[2]/div/a'
# if not driver.find_element(By.XPATH, product_xpath).is_displayed():
#     raise Exception("Product is not displayed")
#
# drop_down = '#post-7 > div > div > div:nth-child(4) > div > div > div.wc-block-components-sidebar.wc-block-cart__sidebar.wp-block-woocommerce-cart-totals-block > div.wp-block-woocommerce-cart-order-summary-block > div.wp-block-woocommerce-cart-order-summary-coupon-form-block.wc-block-components-totals-wrapper > div > div:nth-child(1) > button > svg'
# # for i in range(5):
# #     try:
# #         driver.find_element(By.XPATH, drop_down)
# #     except:
# #         print("Retrying...")
# #         time.sleep(2)
# #         driver.refresh()
#
# driver.find_element(By.CSS_SELECTOR, drop_down).click()
#
#
# driver.find_element(By.ID,'wc-block-components-totals-coupon__input-0').send_keys('wefguwefg')
# driver.find_element(By.ID,'wc-block-components-totals-coupon__form').click()
#
# # the flow ends here

product_details = []
# Web scrapping
all_products = driver.find_elements(By.CLASS_NAME,'product-type-simple')
print(len(all_products))
for product in all_products:
    price = product.find_element(By.CSS_SELECTOR,'span.amount')
    price_valu = price.text

    name = product.find_element(By.CSS_SELECTOR,'h2.woocommerce-loop-product__title').text
    product_details.append({'name':name,'price':price_valu})

print(product_details)
# driver.quit()