import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# import org.openqa.selenium.Keys

nameofsong=input('>>>>')

browser = webdriver.Chrome()
# driver = webdriver.Firefox()
browser.get('https://www.saavn.com/')
song=browser.find_element_by_xpath("//input[@id='search']")
song.send_keys(nameofsong)
song.send_keys(u'\ue007')
new_s=browser.find_element_by_xpath("//html//li[1]/div[2]")
# new_s=browser.find_element_by_class_name('_class="title"')

actionChains = ActionChains(browser)
actionChains.click(new_s).perform()
# new_s=browser.find_element_by_name('feels')



# driver.quit()b

