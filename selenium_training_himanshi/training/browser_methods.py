import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

#launch the application
driver.get("https://www.myntra.com/")
time.sleep(2)

#to maximize the window
driver.maximize_window()
time.sleep(2)

# to minimize the window
# driver.minimize_window()

# To go back
driver.back()
time.sleep(2)

# To go forward
driver.forward()
time.sleep(2)

# To refresh
driver.refresh()

# current_url
print(driver.current_url)

# title
print(driver.title)

# name
print(driver.name)

# page_source
print(driver.page_source)

# To take the screenshots

# driver.save_screenshot("myntra_homepage.png")
# The screenshot will be saved in the same package as our python file


# To save the screenshots in different location
# driver.save_screenshot(r'C:\Users\KIIT\Downloads\selenium_training\selenium_training_himanshi\files')


driver.close()




















