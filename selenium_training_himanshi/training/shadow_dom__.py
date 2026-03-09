
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://the-internet.herokuapp.com/shadowdom")
time.sleep(2)

shadow_ele = driver.find_element("css selector", "my-paragraph")
host = shadow_ele.shadow_root
data = host.find_element('css selector', 'p')
print(data.text)




































































