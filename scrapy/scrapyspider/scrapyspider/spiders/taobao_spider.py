# -*- coding: UTF-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import TaobaoItem
import re
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver

import chardet
class TaobaoTshirt_Spider(Spider):
	name ='taobao1'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	}
	item = TaobaoItem()
	def start_requests(self):
		print '+++++++++'
		url = 'https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&ntoffset=6&s=0'
		yield Request(url,headers =self.headers)
	def parse(self,response):
		fo = open('test.log','w')
		sys.stdout = fo
		print '============================='
		datas = response.xpath('//script/text()').extract() 
		#item = TaobaoItem()
		if datas:
			pattern = re.compile('"raw_title":"(.*?)",.*?"detail_url":"(.*?)",.*?"view_price":"(.*?)",.*?"item_loc":"(.*?)","view_sales":"(.*?)",.*?"nick":"(.*?)",',re.S)
			contents = re.findall(pattern,str(datas))
			for content in contents:
				#import chardet
				#fencoding=chardet.detect(content[4])
				#print fencoding
				print content[5].decode("unicode_escape").encode('utf-8')
				print content[3].decode("unicode_escape").encode('utf-8')
				print content[0].decode("unicode_escape").encode('utf-8')
				print content[2].decode("unicode_escape").encode('utf-8')
				print content[4].decode("unicode_escape").encode('utf-8')
				print content[1]
				print '============================='
				detail_url = 'https:'+ content[1].decode('unicode_escape').decode("unicode_escape").encode('utf-8')
				print detail_url
				self.get_details(detail_url)
				#item['month_sales'] = results[0].text
				#item['reviews'] = results[1].text
				self.item['store_name'] =content[5].decode("unicode_escape").encode('utf-8')
				self.item['store_location'] =content[3].decode("unicode_escape").encode('utf-8')
				self.item['goods_name'] =content[0].decode("unicode_escape").encode('utf-8')
				self.item['price'] =content[2].decode("unicode_escape").encode('utf-8')
				self.item['sales'] =content[4].decode("unicode_escape").encode('utf-8')
				
				yield self.item
	def get_details(self,url):
		browser = webdriver.Chrome()#PhantomJS
		browser.get(url)
		time.sleep(2)
		print '=================================6666666666!!!!'
		try:
			results = browser.find_elements_by_xpath("//span[@class='tm-count']")
			print u'month_sales:',results[0].text
			print u'review_num:',results[1].text
			
			self.item['month_sales'] = results[0].text
			self.item['reviews'] = results[1].text
		except:
			results = browser.find_elements_by_xpath("//em[@class='J_ReviewsCount']")
			print u'未知月销量'
			print u'review_num:',results[0].text
			self.item['month_sales'] = u'未知'
			self.item['reviews'] = results[0].text
		else:
			print u'ok=====go on '
		browser.quit()
		
		

#url = https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&ntoffset=6&s=0
#https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend
#=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017
#.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc
#&bcoffset=0&p4ppushleft=%2C44&s=44
