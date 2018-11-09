import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

video=input('>>>>')

browser = webdriver.Chrome()
# driver = webdriver.Firefox()
browser.get('https://www.youtube.com/')
song=browser.find_element_by_xpath("//input[@id='search']")
song.send_keys(video)
song.send_keys(u'\ue007')
new_s=browser.find_element_by_xpath("//html//ytd-video-renderer[1]/div[1]/ytd-thumbnail[1]/a[1]/yt-img-shadow[1]/img[1]")
# new_s=browser.find_element_by_class_name('_class="title"')

actionChains = ActionChains(browser)
actionChains.click(new_s).perform()




# driver.quit()b

