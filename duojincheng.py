import multiprocessing
import time
def process(num):
	time.sleep(num)
	print 'process:',num
	
if __name__ == '__main__':
	for i in range(5):
		p = multiprocessing.Process(target=process,args=(i,))
		p.start()
	print ('cpu number:'+str(multiprocessing.cpu_count()))
	for p in multiprocessing.active_children():
		print ('Child process name: ' + p.name + ' id: ' + str(p.pid))
	
	print 'finished'