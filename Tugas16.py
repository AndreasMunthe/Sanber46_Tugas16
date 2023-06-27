
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver1=webdriver.Chrome(options=options)
driver1.get("https://www.saucedemo.com/")

#Browser Maximize
driver1.maximize_window()

#Login and Logout Succes (Scenario 1)

# steps
driver1.find_element(By.NAME,"user-name").send_keys("standard_user") # isi email
time.sleep(1)
driver1.find_element(By.NAME,"password").send_keys("secret_sauce") # isi password
time.sleep(1)
driver1.find_element(By.NAME, "login-button").click()
time.sleep(1)
driver1.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver1.find_element(By.ID, "logout_sidebar_link").click()  

time.sleep(5)

#Failed login username is empty (Scenario 2)
driver1.get("https://www.saucedemo.com/")
time.sleep(1)
driver1.find_element(By.NAME,"user-name").send_keys("") # email tidak terisi
time.sleep(1)
driver1.find_element(By.NAME,"password").send_keys("secret_sauce") # isi password
time.sleep(1)
driver1.find_element(By.NAME, "login-button").click()
time.sleep(1)

time.sleep(5)
#Failed login Password is empty(Scenario 3)
driver1.get("https://www.saucedemo.com/")
time.sleep(1)
driver1.find_element(By.NAME,"user-name").send_keys("standard_user") # email tidak terisi
time.sleep(1)
driver1.find_element(By.NAME,"password").send_keys("") # isi password
time.sleep(1)
driver1.find_element(By.NAME, "login-button").click()
time.sleep(1)

#Failed login Username & Password  is empty(Scenario 4)
driver1.get("https://www.saucedemo.com/")
time.sleep(1)
driver1.find_element(By.NAME,"user-name").send_keys("") # email tidak terisi
time.sleep(1)
driver1.find_element(By.NAME,"password").send_keys("") # isi password
time.sleep(1)
driver1.find_element(By.NAME, "login-button").click()
time.sleep(1)

driver1.close()