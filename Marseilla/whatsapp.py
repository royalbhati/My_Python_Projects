from selenium import webdriver

profile=webdriver.FirefoxProfile()
driver = webdriver.Firefox()
driver.get('http://web.whatsapp.com')

# name = input('Enter the name of user or group : ')
# msg = input('Enter the message : ')
# count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format('cc'))
user.click()

msg_box = driver.find_element_by_class_name('input-container')

for i in range(5):
    msg_box.send_keys('howdy')
    driver.find_element_by_class_name('compose-btn-send').click()
