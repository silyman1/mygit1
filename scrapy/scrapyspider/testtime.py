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
browser.get('//rate.taobao.com/user-rate-95cf5ce4398a3bd471b08cbe9bf6e0fb.htm?spm=2013.1.1000126.10.68ab26c2ws4Vvj')
#browser=webdriver.PhantomJS(service_args=['--ssl-protocol=any'])#PhantomJS
#browser.get(url)
time.sleep(5)
decribe_score = browser.find_element_by_xpath('//*[@id="dsr"]/li[1]/div[1]/em[1]')
print 'decribe_score:',decribe_score
attitude_score = browser.find_element_by_xpath('//*[@id="dsr"]/li[2]/div[1]/em[1]')
print 'attitude_score:',attitude_score
logistics_score = browser.find_element_by_xpath('//*[@id="dsr"]/li[3]/div[1]/em[1]')
print 'logistics_score:',logistics_score
store_rating = browser.find_element_by_xpath('//*[@id="dsr"]/li[2]/div[2]/div/div[1]/em')
print 'store_rating:',store_rating
browser.quit()

