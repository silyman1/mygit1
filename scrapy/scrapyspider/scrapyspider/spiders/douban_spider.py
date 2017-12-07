# -*- coding: UTF-8 -*-
import sys
from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem
from bs4 import BeautifulSoup
class DoubanMovieTop250Spider(Spider):
	name = 'douban_movie_top250'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	}
	def start_requests(self):
		url = 'https://movie.douban.com/top250'
		yield Request(url, headers=self.headers)
	def parse(self, response):
		# 命令行调试代码
		#from scrapy.shell import inspect_response
		#inspect_response(response, self)
		print "###############1######################beginning########"
		html = response.body.decode('utf-8')
		url = 'https://movie.douban.com/top250'
		soup = BeautifulSoup(html)
		fo = open('test.log','w')
		sys.stdout = fo
		movies = soup.find_all('div',class_="item")
		item = DoubanMovieItem()
		for movie in movies:
			item['ranking'] = movie.em.string
			item['movie_name'] = movie.find('span',class_="title").string
			item['score'] = movie.find('span',class_="rating_num").string
			item['score_num'] = movie.find('span',property="v:best").next.next.string
			print item
			yield item
		next_url = url + soup.find('link',rel="next").get('href')
		print next_url
		print type(next_url),'1111'
		if next_url:
			yield Request(next_url, headers=self.headers)
		print 'aaaaaaaaaaaaaa'