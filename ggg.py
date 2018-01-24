
import requests
import sys
import json
import time
import re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
fo = open('error.log','w')
sys.stdout = fo
type_list =[]
url= 'https://www.bilibili.com/'
response = requests.get(url)
soup  =BeautifulSoup(response.text)
items = soup.find_all('li',class_='nav-item')
print '33'
for item in items:
	try:
		print '3'
		type = item.find('div',attrs={'class':'nav-name'}).text
		print type
		detail_types =item.find_all('li',attrs={'class':'sub-nav-item'})
		print detail_types
	except:
		continue
	detail_types=[i.text for i in detail_types]
	type_list.append((type,detail_types))