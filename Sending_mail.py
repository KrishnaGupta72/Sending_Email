import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:/PyCharm Projects/chromedriver.exe")

#----------------Input Section-----------------------------------
Uname=input("To continue to Gmail, Please enter Email or Phone: ")
Pwd=input("Please enter your Password: ")
to=input("Please enter email to whom to want to send: ")
subject=input("Please enter your email subject: ")
mail_body=input("Please enter your email body: ")
#----------------Input Section-----------------------------------

#Hitting google.com
driver.get('http://www.gmail.com')
time.sleep(2)
#Finding Username_input_box
Uname_input_box = driver.find_element_by_xpath('//input[@type="email"]')
Uname_input_box.clear()
# Pass username value to input box.
Uname_input_box.send_keys(Uname)
time.sleep(2)
Uname_input_box.send_keys(Keys.RETURN)
time.sleep(4)

#Finding Password_input_box
Pwd_input_box = driver.find_element_by_xpath('//input[@type="password"]')
Pwd_input_box.clear()
# Pass password value to input box.
Pwd_input_box.send_keys(Pwd)
time.sleep(2)
Pwd_input_box.send_keys(Keys.RETURN)
time.sleep(10)

#Finding and clicking compose button element
Compose_button = driver.find_element_by_xpath('//div[@class="z0"]/div[@role="button"]')
time.sleep(5)
Compose_button.click()

#Finding and filling To_Text_area element
To_Text_area = driver.find_element_by_xpath('//div[@class="wO nr l1"]//textarea[@class="vO"]')
To_Text_area.send_keys(to)
time.sleep(5)

#Finding and filling Subject_input_box element
Sub_input_box = driver.find_element_by_xpath('//div[@class="aoD az6"]/input[@name="subjectbox"]')
Sub_input_box.send_keys(subject)
time.sleep(2)

#Finding and filling mail_body_textbox element
mail_body_textbox = driver.find_element_by_xpath('//div[@role="textbox"]')
mail_body_textbox.send_keys(mail_body)
time.sleep(2)
mail_body_textbox.send_keys(Keys.RETURN)
time.sleep(4)

#Finding and clicking sendmail_butto element.
send_button = driver.find_element_by_xpath('//div[@id=":7v"]/div[@role="button"]')
send_button.click()
