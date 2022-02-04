import time
from selenium import webdriver
import pytest
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Firefox()
driver.maximize_window()

######## STEP - 1 ##########
URL = "https://rapsodo.com/"
driver.get(URL)
print("Step 1 Success")

######## STEP - 2 ##########
driver.find_element(By.LINK_TEXT, "GOLF").click()
driver.get("https://rapsodo.com/golf/mlm/")

get_title = driver.title
title_value = "Golf Swing Analyzer | Improve Your Swing | Rapsodo"

if get_title == title_value:
    print("Step 2.a Success")
else:
    print("Step 2.a Failed")


get_descripton = driver.find_element(By.CSS_SELECTOR, ".Description").text
description = "0 items - $0.00"

if get_descripton == description:
    print("Step 2.b Success")
else:
    print("Step 2.b Failed")


######## STEP - 3 ##########
driver.find_element(By.LINK_TEXT, "SHOP NOW").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".ast-col-sm-12:nth-child(1) .attachment-woocommerce_thumbnail").click()

get_monitor_url = driver.execute_script("return window.location.href")
monitor_url_value = "mobile-launch-monitor"

if monitor_url_value in get_monitor_url:
    print("Step 3.a Success")
else:
    print("Step 3.b Success")


######## STEP - 4 ##########
time.sleep(3)
driver.find_element(By.NAME, "quantity").send_keys(Keys.CONTROL + "a")

time.sleep(3)
driver.find_element(By.NAME, "quantity").send_keys(Keys.DELETE)

time.sleep(3)
driver.find_element(By.NAME, "quantity").send_keys("2")
time.sleep(3)

driver.find_element(By.ID, "cookie_action_close_header").click()
time.sleep(3)
driver.find_element(By.NAME, "add-to-cart").click()

time.sleep(3)
get_cart_url = driver.execute_script("return window.location.href")
cart_url_value = "cart"

if cart_url_value in get_cart_url:
    print("Step 4.a Success")
else:
    print("Step 4.b Success")



######## STEP - 5 ##########
time.sleep(3)
driver.find_element(By.LINK_TEXT, "View Cart").click()

get_total_cost =driver.find_element(By.CSS_SELECTOR, ".order-total > td:nth-child(2) > strong:nth-child(1) > span:nth-child(1) > bdi:nth-child(1)").text
time.sleep(3)
get_one_cost = driver.find_element(By.CSS_SELECTOR, "td.product-price > span:nth-child(1) > bdi:nth-child(1)").text


get_total_cost2 = float(get_total_cost.replace("$",""))
get_one_cost2 = float(get_one_cost.replace("$",""))

quantity = (get_total_cost2/get_one_cost2)

quantity_value = 2
costs = "$999.98"

if quantity == quantity_value:
        if get_total_cost == costs:
              print("Step 5.a Success")
else:
    print("Step 5.a Failed")



######## STEP - 6 ##########

driver.find_element(By.ID, "coupon_code").click()

driver.find_element(By.ID, "coupon_code").send_keys("GOLFTHEBEST")

driver.find_element(By.NAME, "apply_coupon").click()
time.sleep(5)
error_get = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error > li").text

error_value = 'Coupon "golfthebest" does not exist!'

if error_get == error_value:
    print("Step 6.a Success")
else:
    print("Step 6.a Failed")



######## STEP - 7 ##########
driver.close()
print("Step 7 Success")

