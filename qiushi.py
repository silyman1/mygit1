#coding=utf-8
import requests
from bs4 import BeautifulSoup
from Queue import Queue
import threading
import datetime
import time
import json
import re

#抓取线程类
class Thread_Crawler(threading.Thread):
	def __init__(self,thread_id,page_queue,data_queue):
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.page_queue = page_queue
		self.data_queue = data_queue
		self.headers =headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                    'Accept-Language': 'zh-CN,zh;q=0.8'}
	def run(self):
		print u"爬取线程%s 启动...."%self.thread_id
		self.qiushi_spider()
		self.page_queue.task_done()
		print u"爬取线程%s 关闭...."%self.thread_id
	def qiushi_spider(self):
		while True:
			if self.page_queue.empty():
				break
			else:
				page = self.page_queue.get()
				print u"爬虫线程%s 爬取page=%d...."%(self.thread_id,page)
				url =  'http://www.qiushibaike.com/hot/page/' + str(page) + '/'
				timeout = 5
				while timeout > 0:
					try:
						response = requests.get(url,headers=self.headers)
						self.data_queue.put(response.text)
						break
					except Exception,e:
						print 'qiushi_spider__error:',e
						
				if timeout <0:
					print 'timeout:',url
#解析线程类
class Thread_Parser(threading.Thread):
	def __init__(self,thread_id,data_queue,output_queue,lock,output):
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.data_queue = data_queue
		self.output_queue= output_queue
		self.lock = lock
		self.output =output
	def run(self):
		global total_count ,exitflag
		print u"解析页面线程%s 启动...."%self.thread_id
		while not exitflag:
			try:
				item =self.data_queue.get(False)
				self.parse_page(item)
				self.data_queue.task_done()
				print u"解析页面线程%s ....当前解析页面总数为%d"%(self.thread_id,total_count)
			except:
				pass
		print u"解析页面线程%s 关闭...."%self.thread_id
	def parse_page(self,item):
		global total_count
		try:
			soup =BeautifulSoup(item)
			#results = soup.find_all('div',attrs={"class":'article block untagged mb15'})
			results = soup.find_all('div',attrs={"id":re.compile(r"qiushi_tag_(\w+)")})
			#results = soup.find_all('div',attrs={"class":re.compile(r"article block untagged mb15(\s)")})
			print len(results)
			try:
				for result in results:
					author = result.find("h2").text
					content =result.find("div",attrs={"class":"content"})
					content = content.find("span").text.split()
					votes = result.find("span",attrs={"class":"stats-vote"}).text
					comments =result.find("span",attrs={"class":"dash"}).text
					output_item = {"author":author,
									"content":content,
									"votes":votes,
									"comments":comments,}
					#self.output_queue.put(output_item)
					with self.lock:
						self.output.write(json.dumps(output_item,ensure_ascii=False).encode('utf-8')+',\n')
				with self.lock:
					total_count += 1
			except Exception,e:
				print "parse detail error...",e
		except Exception,e:
			print 'parse result error:',e
#class Write_Thread(threading.Thread):
	
########################
exitflag =False
total_count = 0
lock = threading.Lock()

def main():
	output = open('qiushibaike.json', 'a')
	data_queue = Queue()
	output_queue = Queue()
	page_queue = Queue()
	for i in range(1,11):
		page_queue.put(i)

	crawlthreads = []
	crawllist = ["crawl-1", "crawl-2", "crawl-3"]
	for thread_id in crawllist:
		thread = Thread_Crawler(thread_id,page_queue,data_queue)
		thread.start()
		crawlthreads.append(thread)
	global lock
	parserthreads = []
	parserlist = ["parser-1", "parser-2", "parser-3"]
	for threadID in parserlist:
		thread = Thread_Parser(threadID, data_queue,output_queue,lock,output)
		thread.start()
		parserthreads.append(thread)
	while not page_queue.empty():
		pass
	for t in crawlthreads:
		t.join()
	while not data_queue.empty():
		pass
	global exitflag
	exitflag = True
	
	for t in parserthreads:
		t.join()
	
	print u"主进程结束。。。。。"
	with lock:
		output.close()
if __name__ =="__main__":
	main()