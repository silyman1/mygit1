# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
#fo = open('111.log','w')
#sys.stdout = fo

browser = webdriver.Chrome()
#browser=webdriver.PhantomJS(service_args=['--ssl-protocol=any'])#PhantomJS
browser.get('https://detail.tmall.com/item.htm?spm=a230r.1.14.5.5144467egnPC4G&id=557649706137&ns=1&abbucket=20')
time.sleep(3)
browser.save_screenshot('E:\\mygit1\\scrapy\\scrapyspider\\1123.png')
#try:
	#results = browser.find_elements_by_xpath("//span[@class='tm-count']")
	#print u'month_sales:',results[0].text
	#print u'review_num:',results[1].text

#except:
	#ults = browser.find_elements_by_xpath("//em[@class='J_ReviewsCount']")
	#print u'未知月销量'
	#print u'review_num:',results[0].text

#else:
	#print u'ok=====go on '

score_urls = browser.find_elements_by_xpath('//*[@class="main-info"]/a')

for score_url in score_urls:
	print score_url.get_attribute("href")
#print browser.page_source
#for score_url in score_urls:
	#print score_url.find_element_by_xpath("//a").get_attribute("href")
browser.quit()

