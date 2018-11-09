import requests
from bs4 import BeautifulSoup



def weathercheck():
	urll=requests.get('https://weather.com/en-IN/weather/today/l/28.66,77.23').text


	soup=BeautifulSoup(urll,'lxml')

	temperature=soup.find('div',class_='today_nowcard-temp')
	findplace=soup.find('h1',class_='h4 today_nowcard-location')
	place=findplace.text
	today=temperature.span.text
	print(place)
	print(today+"C")



if __name__ == '__main__':
	
	weathercheck()
