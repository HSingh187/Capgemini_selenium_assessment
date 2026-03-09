import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## gives an alert
# time.sleep(2)
#
# switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# To accept the alert
# alert_obj.accept()
# time.sleep(2)
#
# To dismiss the alert
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

'''
simple alert         
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

'''
prompt alert        
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# ## enter the data
# alert_obj.send_keys("Rohit")
#
# alert_obj.accept()

'''
Authentication popup     
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')


# ## To handle the authentication popups, we use the below syntax
# ## SYNTAX   :   https://username:password@url
# ## For the below url, username and password is both admin
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

''' PUSH NOTIFICATION '''

#  Chrome
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.irctc.co.in/nget/train-search")

#Firefox
from selenium import webdriver

opts = webdriver.FirefoxOptions()
opts.set_preference("dom.webnotifications.enabled", False)
opts.set_preference("dom.push.enabled", False)

driver = webdriver.Firefox(opts)

driver.get("https://www.irctc.co.in/nget/train-search")

# Edge
from selenium import webdriver

opts = webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Edge(opts)

driver.get("https://www.irctc.co.in/nget/train-search")




































































































