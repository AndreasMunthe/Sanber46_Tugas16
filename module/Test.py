from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#from selenium.webdriver import ActionChains
#from selenium.webdriver.common.keys import Keys
import time
#from selenium.webdriver import Chrome
f#rom selenium.webdriver.chrome.service import Service

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver1=webdriver.Chrome(options=options)
driver1.get("http://www.thetestingWorld.com/testings")

"""
#driver1.find_element(By.NAME, 'username').send_keys('iasdiasid')
#driver1.find_element(By.PARTIAL_LINK_TEXT,"Elemental").click()

# Get element with tag name 'div'
#element = driver1.find_element(By.TAG_NAME, 'div')

# Get all the elements available with tag name 'p'
elements = driver1.find_elements(By.TAG_NAME, 'a')
for e in elements:
    print(len(elements))

#driver1.find_element(By.CLASS_NAME,'radius').click()

#time.sleep(5)

# Get element with XPATH
#driver1.find_element(By.XPATH,'//*[@id="login"]/button').click()

# Get an auto screenshoot
#driver1.get_screenshot_as_file("C:\\Lets Work\\Capture\\capture.png")

# Get element with link text
#driver1.find_element(By.LINK_TEXT,'Click Here').click()

#Switch tab
#driver1.switch_to.window(driver1.window_handles[0])

#Get element with id
action=ActionChains(driver1)
square=driver1.find_element(By.XPATH,'//*[@id="hot-spot"]')

action.context_click(square).perform()
time.sleep(3)
driver1.maximize_window()
"""
#Maximize browser

driver1.maximize_window()
print("Succes maximize page")

driver1.find_element(By.NAME,'fld_username').send_keys('George')
driver1.find_element(By.XPATH,'//*[@id="tab-content1"]/form/input[3]').send_keys('xxxxxx@gmail.com')
driver1.find_element(By.NAME,'fld_password').send_keys('123582f')
driver1.find_element(By.NAME,'fld_cpassword').send_keys('123582f')
driver1.find_element(By.NAME,'fld_username').clear()
driver1.find_element(By.NAME,'fld_username').send_keys('Jaya')

#Fill Radio Button
driver1.find_element(By.XPATH,'//input[@value="home"]').click()

#Select on Checkbox
driver1.find_element(By.NAME,'terms').click()

#Click link a href
#driver1.find_element(By.LINK_TEXT,"Read Detail").click()

#Click on Button
#driver1.find_element(By.XPATH,'//input[@type="submit"]').click()

#Select on dropdown
obj=Select(driver1.find_element(By.NAME,'sex'))
obj.select_by_index(1)
obj.select_by_index(2)



