# -*- coding: UTF-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import TaobaoItem
import re
import sys


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
			pattern = re.compile('"raw_title":"(.*?)",.*?"view_price":"(.*?)",.*?"item_loc":"(.*?)","view_sales":"(.*?)",.*?"nick":"(.*?)",',re.S)
			contents = re.findall(pattern,str(datas))
			for content in contents:
				#import chardet
				#fencoding=chardet.detect(content[4])
				#print fencoding
				print content[4].decode("unicode_escape").encode('utf-8')
				print content[2].decode("unicode_escape").encode('utf-8')
				print content[0].decode("unicode_escape").encode('utf-8')
				print content[1].decode("unicode_escape").encode('utf-8')
				print content[3].decode("unicode_escape").encode('utf-8')
				print '============================='
				item['store_name'] =content[4].decode("unicode_escape").encode('utf-8')
				item['store_location'] =content[2].decode("unicode_escape").encode('utf-8')
				item['goods_name'] =content[0].decode("unicode_escape").encode('utf-8')
				item['price'] =content[1].decode("unicode_escape").encode('utf-8')
				item['sales'] =content[3].decode("unicode_escape").encode('utf-8')
				yield item


#url = https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&ntoffset=6&s=0
#https://s.taobao.com/search?q=t%E6%81%A4&imgfile=&commend
#=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017
#.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc
#&bcoffset=0&p4ppushleft=%2C44&s=44
