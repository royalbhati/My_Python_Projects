
import twittermodule



def reddit():
	tts=gTTS(text='opening reddit',lang='hi')
	tts.save('reddit.mp3')
	os.system('mpg321 reddit.mp3')
	browse=webdriver.Chrome()
	browse.get('https://www.reddit.com/')
	username=''
	password=''
	browse.find_element_by_xpath('id("login_login-main")/input[2]').clear()
	browse.find_element_by_xpath('id("login_login-main")/input[2]').send_keys(username)
	browse.find_element_by_xpath('id("login_login-main")/input[3]').clear()
	browse.find_element_by_xpath('id("login_login-main")/input[3]').send_keys(password)
	browse.find_element_by_xpath('id("login_login-main")/div[4]/button[1]').click()	

def byee():
	tts=gTTS(text='Baabayee',lang='en')
	tts.save('beyee.mp3')
	os.system('mpg321 beyee.mp3')	
	exit()

def google():
	tts=gTTS(text='okay and What you want to search?')
	tts.save('google.mp3')
	os.system('mpg321 google.mp3')
with sr.Microphone() as source:
	audio=r.listen(source)
	browser=webdriver.Chrome()
	browser.get('https://www.google.com/')

	browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(r.recognize_google(audio))
	browser.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(Keys.RETURN);			

def twitter():
	tts=gTTS(text='What do yo want me to do')
	tts.save('twitter.mp3')
	os.system('mpg321 twitter.mp3')
	blit()

def hello(name):
	tts=gTTS(text='Hi '+name+' How are you',lang='hi')
	tts.save("goo.mp3")
	os.system("mpg321 goo.mp3")	

def weather():

	urll=requests.get('https://weather.com/en-IN/weather/today/l/28.66,77.23').text


	soup=BeautifulSoup(urll,'lxml')

	temperature=soup.find('div',class_='today_nowcard-temp')
	findplace=soup.find('h1',class_='h4 today_nowcard-location')
	place=findplace.text
	today=temperature.span.text
	print(place)
	print(today+"C")






