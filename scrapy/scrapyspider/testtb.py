# -*- coding: UTF-8 -*-
import urllib2
import sys
import json

fo = open('testtaobao.log','w')
sys.stdout = fo

url = url = 'https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&ntoffset=6&s=0'
headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	}
request = urllib2.Request(url,headers =headers )
response = urllib2.urlopen(request)

print '+++++++++++++++++++++++++++++++'
print response.body