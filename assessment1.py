import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)
wait = WebDriverWait(driver,10)

#1
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
driver.find_element("xpath","//a[contains(text(),'Books')]").click()
time.sleep(2)
driver.find_element("xpath","(//input[@value='Add to cart'])[1]").click()
time.sleep(2)
driver.find_element("xpath","//span[@class='close']").click()
time.sleep(1)
driver.find_element("xpath","//span[text()='Shopping cart']").click()
time.sleep(2)
product = driver.find_element("xpath","//table[@class='cart']")
print(product.is_displayed())
time.sleep(2)

#2
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
electronics = driver.find_element("xpath","//a[contains(text(),'Electronics')]")
ac.move_to_element(electronics).perform()
time.sleep(2)
driver.find_element("xpath","//a[contains(text(),'Cell phones')]").click()
time.sleep(2)

#3
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element("xpath","//button[text()='Start']").click()
text = wait.until(EC.visibility_of_element_located(("xpath","//h4[text()='Hello World!']")))
print(text.text)

#4
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.find_element("xpath","//button[text()='Remove']").click()
add_btn = wait.until(EC.element_to_be_clickable(("xpath","//button[text()='Add']")))
add_btn.click()

#5
driver.get("https://demoqa.com/select-menu")
wait = WebDriverWait(driver, 10)
dropdown = driver.find_element('xpath', '//div[@id="withOptGroup"]')
driver.execute_script("arguments[0].scrollIntoView();", dropdown)

wait.until(EC.element_to_be_clickable(dropdown)).click()

option = driver.find_element('xpath', '//div[text()="Group 2, option 1"]')
wait.until(EC.element_to_be_clickable(option)).click()

selected = driver.find_element('xpath', '//div[contains(@class,"singleValue")]')
wait.until(EC.visibility_of(selected))

print("Selected value:", selected.text)
#6
driver.get("https://demoqa.com/select-menu")
driver.execute_script("window.scrollBy(0,600)")
multi = Select(driver.find_element("xpath","//select[@id='cars']"))
multi.select_by_visible_text("Volvo")
multi.select_by_visible_text("Saab")
multi.select_by_visible_text("Opel")
for i in multi.all_selected_options:
    print(i.text)

#7
driver.get("https://demoqa.com/menu/")
time.sleep(2)
main = driver.find_element("xpath","//a[text()='Main Item 2']")
sub = driver.find_element("xpath","//a[text()='SUB SUB LIST »']")
sub1 = driver.find_element("xpath","//a[text()='Sub Sub Item 1']")
ac.move_to_element(main).move_to_element(sub).click(sub1).perform()

#8
driver.get("https://demoqa.com/droppable")
time.sleep(2)
draggable_ele = driver.find_element('xpath', '//div[text()="Drag Me"]')
droppable_ele = driver.find_element('xpath', '//p[text()="Drop Here"]')
ac.drag_and_drop(draggable_ele, droppable_ele).perform()

#9
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element("xpath","//button[text()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
time.sleep(2)
alert.accept()
print(driver.find_element("xpath","//p[@id='result']").text)

#10
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element("xpath","//input[@id='file-upload']").send_keys("C:\\Users\\KIIT\\Downloads\\test.txt")
driver.find_element("xpath","//input[@id='file-submit']").click()
print(driver.find_element("xpath","//div[@id='uploaded-files']").text)

#13
driver.get("https://demowebshop.tricentis.com")
driver.find_element('xpath', '//a[contains(text(),"Books")]').click()
time.sleep(2)
books = driver.find_elements('xpath', '//div[@class="item-box"]')
for book in books:
    price = book.find_element('xpath', './/span[@class="price actual-price"]').text
    price = float(price.replace("$", ""))
    if price < 20:
        try:
            button = book.find_element('xpath', './/input[@value="Add to cart"]')
            button.click()
            print("Added book with price:", price)
            time.sleep(1)
        except:
            pass