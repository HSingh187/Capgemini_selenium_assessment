import time
import xlrd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(opts)

ac = ActionChains(driver)
#################################################1#############################################################
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//input[@name="email"]').send_keys("Himanshi")
# time.sleep(2)
# driver.find_element('xpath','//input[@name="pass"]').send_keys("password")
# time.sleep(2)
#
# driver.find_element('xpath','//span[text()="Log in"]').click()
# time.sleep(2)
#
# current_url = driver.current_url
#
# if "login" not in current_url and "facebook.com" in current_url:
#     print("Login Successful")
# else:
#     print("Login Failed")

#################################################2#############################################################
# driver.maximize_window()
#
# driver.get("https://www.myntra.com")
# time.sleep(5)
#
# wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.presence_of_element_located(('xpath', '//input[@placeholder="Search for products, brands and more"]')))
# search_box.send_keys("puma")
#
#
# suggestion = wait.until(EC.presence_of_element_located(
#     ('xpath', '//li[contains(@class,"desktop-suggestion")][2]')
# ))
# suggestion.click()
#
# product = wait.until(EC.presence_of_element_located(
#     ('xpath', '(//li[@class="product-base"])[1]')
# ))
# product.click()
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# shoe_size = wait.until(EC.element_to_be_clickable(
#     ('xpath','//p[text()="8"]')
# ))
# time.sleep(5)
# add_to_bag = wait.until(EC.element_to_be_clickable(
#     ('xpath', '//div[text()="ADD TO BAG"]')
# ))
# time.sleep(2)
#
# shoe_size.click()
# add_to_bag.click()
#
# print("Product added to cart successfully!")

#################################################3#############################################################
# driver.maximize_window()
#
# driver.get("https://www.icici.bank.in/")
# time.sleep(5)
#
# driver.find_element("xpath", "//span[contains(text(),'Accounts')]").click()
# time.sleep(7)
#
# driver.find_element("xpath", "(//a[contains(text(),'APPLY*')])[2]").click()
# time.sleep(5)
#
# driver.switch_to.window(driver.window_handles[-1])
# time.sleep(5)
#
# driver.find_element(By.ID, "name").send_keys("Himanshi")
# driver.find_element(By.ID, "pan").send_keys("ABCDE1234")
# driver.find_element(By.ID, "pincode").send_keys("751014")
# driver.find_element(By.NAME, "mobile").send_keys("7454935849")
# driver.find_element(By.ID, "resendBtn").click()
# time.sleep(7)
#
# driver.find_element(By.ID, "checkbox").click()
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//button[contains(text(),'Apply Now')]").click()
# time.sleep(5)
#
# try:
#     msg = driver.find_element(By.XPATH, "//*[contains(text(),'invalid') or contains(text(),'error') or contains(text(),'unsuccessful')]").text
#     print("Message:", msg)
# except:
#     print("No error message found")
#
# time.sleep(5)
# driver.quit()

#################################################4#############################################################
# driver.maximize_window()
#
# driver.get("https://www.netmeds.com/")
# time.sleep(5)
#
# actions = ActionChains(driver)
# medicines = driver.find_element("xpath", "//a[contains(text(),'Medicine')]")
# actions.move_to_element(medicines).perform()
# time.sleep(2)
#
# driver.find_element("xpath", "(//a[contains(text(),'Order Online')])[1]").click()
# time.sleep(10)
#
# driver.find_element("xpath", "//button[text()=' Upload Prescription ']").click()
# time.sleep(3)

#################################################5#############################################################
# wait = WebDriverWait(driver, 10)
# driver.get("https://www.netmeds.com/")
# driver.maximize_window()
#
# driver.find_element('xpath','//div[@class="position-relative profile-name"]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@name="mobile-number"]').send_keys("7454935849")
# time.sleep(2)
#
# driver.find_element('xpath','//button[contains(text(),"Get OTP")]').click()
# time.sleep(10)
#
# try:
#     wait.until(EC.visibility_of_element_located(('xpath', '//button[contains(text()," Get started ")]')))
#     print("Login Successful")
# except:
#     print("Login Failed")
#
# time.sleep(2)

#################################################6#############################################################
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@ aria-label="Enter From station. Input is Mandatory."]').send_keys("BBS")
# time.sleep(1)
# driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()
#
# driver.find_element('xpath','//input[@ aria-label="Enter To station. Input is Mandatory."]').send_keys("HYB")
# time.sleep(1)
# driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()
#
# driver.find_element('xpath','//input[@ class="ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]').click()
# driver.find_element('xpath','(//td[@ class="ng-tns-c69-9 ng-star-inserted"])[20]').click()
# time.sleep(1)
#
# driver.find_element('xpath','//div[@ class="ng-tns-c76-10 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
# time.sleep(1)
# driver.find_element('xpath','//li[@ aria-label="AC First Class (1A) "]').click()
#
# driver.find_element('xpath','//div[@ class="ng-tns-c76-11 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
# time.sleep(1)
# driver.find_element('xpath','//li[@ aria-label="TATKAL"]').click()
#
# driver.find_element('xpath','//button[contains(text()," Search Trains ")]').click()

#################################################7#############################################################
# driver.get("https://www.purplle.com/")
# driver.maximize_window()
# time.sleep(3)
#
# brands = driver.find_element('xpath','(//a[@href="/brand"])[1]')
# ac.move_to_element(brands).perform()
# time.sleep(2)
#
# driver.find_element('xpath','//a[contains(text(),"Lakme")]').click()
# time.sleep(3)
#
# first_product = driver.find_element('xpath','(//a[contains(@href,"/product")])[1]')
# ac.scroll_to_element(first_product).perform()
# time.sleep(2)
#
# first_product.click()
# time.sleep(3)
#
# driver.switch_to.window(driver.window_handles[-1])
# time.sleep(5)
#
# driver.find_element('xpath','//input[@name="pincode"]').send_keys("751024")
# time.sleep(2)
#
# driver.find_element('xpath','//button[contains(text(),"Check")]').click()
# time.sleep(2)
#
# print("Pincode availability checked")

#################################################8#############################################################
# from ddt.excel import excel_data
# data = excel_data()
# driver.get('https://lifeinsurance.adityabirlacapital.com/')
# driver.implicitly_wait(10)
# driver.find_element('xpath','(//a[text()="Her Insurance"])[2]').click()
# time.sleep(2)
# driver.find_element('id','firstName').send_keys(data['fname'])
# driver.find_element('id','lastName').send_keys(data['lname'])
# driver.find_element('id','email').send_keys(data['email'])
# driver.find_element('id','phonenumber').send_keys(data['ph'])

#################################################9#############################################################
# driver.get("https://www.apollopharmacy.in/")
# driver.maximize_window()
#
# time.sleep(5) #close all popups manually
#
# driver.find_element('xpath','//a[text()="Find Doctors"]').click()
# time.sleep(2)
# driver.find_element('xpath','//p[text()="General Physician/ Internal Medicine"]').click()
# time.sleep(2)
# visit_doctor = WebDriverWait(driver,15).until(
#     EC.element_to_be_clickable(("xpath","//span[contains(text(),'Visit Doctor')]"))
# )
# visit_doctor.click()
# time.sleep(2)
# driver.find_element('xpath','//p[text()="19"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="11:30 AM"]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Continue"]').click()
# time.sleep(2)
#
# print("Appointment flow executed")

#################################################10#############################################################
# driver.get("https://porter.in/")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('xpath','//p[text()="City:"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="bangalore"]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//div[contains(text(),"Packers & Movers")]').click()
# time.sleep(3)
#
#
# driver.find_element('xpath','//input[@placeholder="Sending from"]').send_keys("Indiranagar")
# time.sleep(2)
# driver.find_element('xpath','(//div[contains(text(),"Indiranagar")])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@placeholder="Sending to"]').send_keys("Whitefield")
# time.sleep(2)
# driver.find_element('xpath','(//div[contains(text(),"Whitefield")])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@placeholder="Enter Contact Details"]').send_keys("3749327498")
# time.sleep(2)
#
# driver.find_element('xpath','//input[@value="18/03/2026"]').click()
# time.sleep(2)
# driver.find_element('xpath','//p[text()="19"]').click() #pass date you want to check for
# time.sleep(2)
# driver.find_element('xpath','(//div[text()="Check Price"])[1]').click()
#
# print("Price check executed")