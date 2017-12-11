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
	
	def start_requests(self):
		print '+++++++++'
		url = 'https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&ntoffset=6&s=0'
		yield Request(url,headers =self.headers)
	def parse(self,response):
		fo = open('test.log','w')
		sys.stdout = fo
		print '============================='
		datas = response.xpath('//script/text()').extract() 
		item = TaobaoItem()
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
				browser = webdriver.PhantomJS()#PhantomJS
				browser.get(detail_url)
				time.sleep(2)
				print '=================================6666666666!!!!'
				#results = browser.find_elements_by_xpath("//span[@class='tm-count']")
				#ime.sleep(1)
				#print u'month_sales:',results[0].text
				#print u'review_num:',results[1].text
				browser.quit()
				#item['month_sales'] = results[0].text
				#item['reviews'] = results[1].text
				item['store_name'] =content[5].decode("unicode_escape").encode('utf-8')
				item['store_location'] =content[3].decode("unicode_escape").encode('utf-8')
				item['goods_name'] =content[0].decode("unicode_escape").encode('utf-8')
				item['price'] =content[2].decode("unicode_escape").encode('utf-8')
				item['sales'] =content[4].decode("unicode_escape").encode('utf-8')
				
				yield item


#url = https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&ntoffset=6&s=0
#https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend
#=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017
#.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc
#&bcoffset=0&p4ppushleft=%2C44&s=44
