# -*- coding: utf-8 -*-
import scrapy 
from scrapy import Request
import json
from scrapy.spiders import Spider
import sys
class WeiboSpider(Spider):

	name = 'weibospider'
	allowded_domains =['weibo.com']
	def start_requests(self):
		url = 'https://m.weibo.cn/p/1005052803301701'
		head1 = 'https://m.weibo.cn/api/container/getIndex?containerid='
		url = head1 + url.replace('https://m.weibo.cn/p/','').replace('100505','107603')
		global url
		yield Request(url)
	def parse(self,response):
		content = json.loads(response.body)
		weibo_info =content.get('cards',[])
		i =0
		fo = open('test.log','w')
		sys.stdout = fo
		for info in weibo_info:
			print '========',i,'========='
			i = i+1
			if info.get('mblog') and info.get('mblog').get('text'):
				title = info.get('mblog').get('text').encode('utf-8')
				secondurl = "https://m.weibo.cn/status/%s" % info["mblog"]["mid"]
				time_recond = info.get('mblog')['created_at'].encode('utf-8')
				picture_urls = ''
				if info.get('mblog').get('page_info'):
					if info.get('mblog').get('page_info').get('media_info'):
						picture_urls =info.get('mblog').get('page_info').get('page_pic')['url']
					print picture_urls,'======================'
				if not picture_urls:
					if info.get('mblog').get('pics'):
						pics = map(lambda x:x.get('url'),info.get('mblog')['pics'])
						picture_urls = ','.join(pics)
			print '++++++++++'
			print title
			print secondurl
			print time_recond
			print picture_urls
			global j
			j=2
			j= j+1
		yield Request(url+)