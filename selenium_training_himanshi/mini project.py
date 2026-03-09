import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.get("https://www.myntra.com/")
time.sleep(3)

parent = driver.current_window_handle

home = driver.find_element('xpath', '//a[@data-group="home"]')
ac.move_to_element(home).perform()
time.sleep(2)

driver.find_element('xpath', '//a[text()="Dinnerware & Serveware"]').click()
time.sleep(3)

driver.find_element('xpath', '(//h4[@class="product-product"])[1]').click()
time.sleep(3)

handles2 = driver.window_handles
print(handles2)

for handle in handles2:
    driver.switch_to.window(handle)
    if "myntra.com" in driver.current_url and handle != parent:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
        time.sleep(2)

driver.switch_to.window(parent)
time.sleep(2)

driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()
time.sleep(3)

handles3 = driver.window_handles
print(handles3)

for handle in handles3:
    driver.switch_to.window(handle)
    if "myntra.com" in driver.current_url and handle != parent:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
        time.sleep(2)
