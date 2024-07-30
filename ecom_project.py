import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\Program Files (x86)\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=PATH)

#initialize webdriver
driver = webdriver.Chrome(service=service)
driver.get("https://tutorialsninja.com/demo/")
time.sleep(10)

phone_button = driver.find_element(By.XPATH, "//*[@id=\"menu\"]/div[2]/ul/li[6]/a")
phone_button.click()
time.sleep(1)


#iphone1
iphone1 = driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[2]/div/div[2]/div[1]/h4/a")
iphone1.click()
time.sleep(1)

#first picture
first_pic = driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div[1]/ul[1]/li[1]")
first_pic.click()
time.sleep(1)

#next picture
next_click = driver.find_element(By.XPATH, "//button[@title = \"Next (Right arrow key)\"]")

for i in range(0,5):
    next_click.click()
    time.sleep(2)

#save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

close_button = driver.find_element(By.XPATH, "//button[@title = \"Close (Esc)\"]")
close_button.click()

time.sleep(2)

#quantity
quantity = driver.find_element(By.ID, "input-quantity")
quantity.click()
quantity.clear()
time.sleep(1)
quantity.send_keys("2")

#Add to cart
add_to_cart = driver.find_element(By.ID, "button-cart")
add_to_cart.click()
time.sleep(2)

#click on cart

cart = driver.find_element(By.ID, "cart-total")
cart.click()
time.sleep(1)

#remove phone

remove = driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[1]/table/tbody/tr/td[5]/button')
remove.click()
time.sleep(1)


#select laptop button
laptop_button = driver.find_element(By.XPATH, "//a[text()= \"Laptops & Notebooks\"]")
action = ActionChains(driver)
action.move_to_element(laptop_button).perform()
time.sleep(2)

all_laptop = driver.find_element(By.XPATH, "//a[text()= \"Show AllLaptops & Notebooks\"]")
all_laptop.click()
time.sleep(2)

#HP laptop
hp_laptop = driver.find_element(By.XPATH, "//a[text()= \"HP LP3065\"]")
hp_laptop.click()



#click on HP laptop 
laptop_add = driver.find_element(By.ID, "button-cart")

#scroll to the button
laptop_add.location_once_scrolled_into_view
time.sleep(1)

#click on calendar for delivery date
calendar_btn = driver.find_element(By.XPATH, '//i[@class= \"fa fa-calendar\"]')
calendar_btn.click()
time.sleep(1)

month_year = driver.find_element(By.XPATH, '//th[text()= "April 2011"]')
right_click = driver.find_element(By.XPATH, '//th[@class= "next"]')

#loop for year: 2022 month: December
while month_year.text != "December 2022":
    right_click.click()

time.sleep(2)

#date 31
date = driver.find_element(By.XPATH, '//td[text()= "31"]')
date.click()
time.sleep(2)

#add to cart button
laptop_add.click()

time.sleep(2)

#click cart

cart_btn = driver.find_element(By.ID, "cart-total")
cart_btn.click()
time.sleep(1)


#checkout button

checkout = driver.find_element(By.XPATH, '//p[@class = "text-right"]/a[2]')
checkout.click()
time.sleep(2)

#guest checkout

guest = driver.find_element(By.XPATH, '//input[@value = "guest"]')
guest.click()
time.sleep(1)

#continue btn

continue_1 = driver.find_element(By.ID, "button-account")
continue_1.click()
time.sleep(1)

#step 2 billing details

billing_detail = driver.find_element(By.XPATH, '//a[text()= "Step 2: Billing Details "]')
billing_detail.location_once_scrolled_into_view
time.sleep(1)

#first name

firstname = driver.find_element(By.ID, "input-payment-firstname")
firstname.click()
time.sleep(1)
firstname.send_keys("Bob")
time.sleep(1)

#last name
lastname = driver.find_element(By.ID, "input-payment-lastname")
lastname.click()
time.sleep(1)
lastname.send_keys("Thomas")
time.sleep(1)

#email
email = driver.find_element(By.ID, "input-payment-email")
email .click()
time.sleep(1)
email .send_keys("bob@gmail.com")
time.sleep(1)

#Telephone
telephone = driver.find_element(By.ID, "input-payment-telephone")
telephone .click()
time.sleep(1)
telephone .send_keys("604 888 8888")
time.sleep(1)

#address
address = driver.find_element(By.ID, "input-payment-address-1")
address.click()
time.sleep(1)
address.send_keys("7731 Albert Street")
time.sleep(1)


#City
city = driver.find_element(By.ID, "input-payment-city")
city.click()
time.sleep(1)
city.send_keys("Toronto")
time.sleep(1)


#PostCode
PostCode = driver.find_element(By.ID, "input-payment-postcode")
PostCode.click()
time.sleep(1)
PostCode.send_keys("M5L N2L")
time.sleep(1)

#country
country = driver.find_element(By.ID, "input-payment-country")
dropdown1 = Select(country)
dropdown1.select_by_index(41)
time.sleep(1)

#Region/state
region= driver.find_element(By.ID, "input-payment-zone")
dropdown2 = Select(region)
time.sleep(1)
dropdown2.select_by_visible_text("Ontario")
time.sleep(1)


#billing detail continue

continue2 = driver.find_element(By.ID, "button-guest")
continue2.click()
time.sleep(1)

#delivery method

continue3 = driver.find_element(By.ID, "button-shipping-method")
continue3.click()
time.sleep(1)

#accept terms and conditions

accept = driver.find_element(By.XPATH, '//input[@name="agree"]')
accept.click()
time.sleep(1)

#continue4

continue4 = driver.find_element(By.ID, "button-payment-method")
continue4.click()
time.sleep(1)

#final price

final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot[1]/tr[3]/td[2]')

print("The final price of both products is: " + final_price.text)
time.sleep(2)

#confirm order
confirm_btn = driver.find_element(By.ID, "button-confirm")
confirm_btn.click()
time.sleep(1)

#display success text

success_text = driver.find_element(By.XPATH, '//*[@id="content"]/h1')
print(success_text.text)
time.sleep(1)

driver.close()



