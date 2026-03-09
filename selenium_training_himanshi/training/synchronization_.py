import time

''' 
Unconditional synchronization
Using time.sleep()
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\KIIT\Downloads\selenium_training\selenium_training_himanshi\files\loading.html')
# time.sleep(20)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')

''' 
Conditional synchronization
Using implicit_wait
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get(r'C:\Users\KIIT\Downloads\selenium_training\selenium_training_himanshi\files\loading.html')
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')

''' 
Conditional synchronization
Using explicit_wait
'''
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 20)
#
#
# driver.get(r'C:\Users\KIIT\Downloads\selenium_training\selenium_training_himanshi\files\loading.html')
#
# wait_obj.until(EC.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauceeee')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
#
# try:
#     wait_obj.until(EC.url_contains("inventory"))
#     print("Valid credentials. Successfull login")
# except:
#     print("Invalid credentials. Unsuccessfull login")


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauceeee')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
#
# try:
#     wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#     print("Valid credentials. Successfull login")
# except:
#     print("Invalid credentials. Unsuccessfull login")

'''
fluent_wait
'''

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[TimeoutException])

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('id', 'user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element('id', 'password').send_keys('secret_sauceeee')
time.sleep(1)
driver.find_element('id', 'login-button').click()
time.sleep(3)

try:
    wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
    print("Valid credentials. Successfull login")
except:
    print("Invalid credentials. Unsuccessfull login")













































































