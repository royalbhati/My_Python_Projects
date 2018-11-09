from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


url=input('Enter URL')
# amazon='https://www.flipkart.com/msi-gl-series-core-i5-8th-gen-8-gb-1-tb-hdd-windows-10-home-4-gb-graphics-gl63-8rc-gaming-laptop/p/itmf48u72wxwyhzx?pid=COMF48U7JHZ93J74&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&lid=LSTCOMF48U7JHZ93J74ZGLHAR&fm=SEARCH&iid=1b2db6b2-cf80-44e7-aa98-89a809ecc33e.COMF48U7JHZ93J74.SEARCH&ppt=Homepage&ppn=Homepage&ssid=6m9sz1t9ao0000001540014801198&qH=3e4c832809293017'

# flipkart='https://www.flipkart.com/msi-gl-series-core-i5-8th-gen-8-gb-1-tb-hdd-windows-10-home-4-gb-graphics-gl63-8rc-gaming-laptop/p/itmf48u72wxwyhzx?pid=COMF48U7JHZ93J74&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&lid=LSTCOMF48U7JHZ93J74ZGLHAR&fm=SEARCH&iid=1b2db6b2-cf80-44e7-aa98-89a809ecc33e.COMF48U7JHZ93J74.SEARCH&ppt=Homepage&ppn=Homepage&ssid=6m9sz1t9ao0000001540014801198&qH=3e4c832809293017'


html = urlopen(url)
bs = BeautifulSoup(html, "html.parser")

!rm -rf prod_comp.csv

try:
	prod_csv=pd.read_csv('prod_comp.csv')
	print(prod_csv)
# 	price_dict=prod_csv.to_dict()

except FileNotFoundError:
	prod_csv=pd.DataFrame({'Name':[],'Price':[]})

prod_csv['Name']=prod_csv['Name'].astype('object')

[i for i in price_dict['Name'].values()]

a=prod_csv['Name'].where(prod_csv['Name']==name.get_text()[25])

pd.Series(name.get_text()[:25])[0]

price = bs.findAll('div', {'class': "_1vC4OE _3qQ9m1"})
names=bs.findAll('span',{'class':"_35KyD6"})
for p in price:
    prod_price=p.get_text()
for name in names:
    if prod_csv['Name'].where(prod_csv['Name']==name.get_text()[25]).empty:
        prod_csv['Name'].append(pd.Series(name.get_text()[:25]))
        prod_csv['Price'].append(pd.Series(prod_price))
        print('Added for monitoring')
    else:
        val=prod_csv['Price'].where(prod_csv['Name']==name.get_text()[25])
        if val>prod_price:
            print('price drop!!!!!')
        else:
        	print('price not chaged')    
        
        


prod_csv

product_csv=pd.DataFrame(price_dict,index=[i for i in range(len(price_dict))])

product_csv



product_csv.to_csv('prod_comp.csv',index=False)

# p=pd.read_csv('temp.csv')
