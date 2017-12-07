# -*- coding: UTF-8 -*-
from scrapy.spiders import Spider

class Blogspider(Spider):
	name = 'teachingspider'
	start_urls = ['http://woodenrobot.me']
	
	def parse(self,response):
		titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
		print "##############beginning########"
		for title in titles:
			print title.strip()