import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.get("https://www.linkedin.com")
time.sleep(2)

## locating the google frame
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')

## switch the driver to the frame
driver.switch_to.frame(google_frame)

## perform the operations inside the frame
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
time.sleep(2)

## switch the driver back to the parent_frame
driver.switch_to.parent_frame()
time.sleep(2)

## scroll down until the youtube ad is visible
ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
ac.scroll_to_element(ele).perform()
time.sleep(2)

## locate the iframe
youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')

## switch the driver to the frame
driver.switch_to.frame(youtube_frame)
time.sleep(2)

## perform the operations inside the frame
driver.find_element('xpath', '//button[@title="Play"]').click()

## switch the driver back to the parent_frame
driver.switch_to.parent_frame()
time.sleep(2)






























































