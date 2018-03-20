import requests 
from multiprocessing.dummy import Pool as ThreadPool 
import time
urls = [
    'http://www.python.org', 
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc.. 
    ]
	
results = [] 
start_time = time.time()
for url in urls:
	result = requests.get(url)
	results.append(result)
print 'Done! Time taken: {}'.format(time.time() - start_time)
# # ------- VERSUS ------- # 


# # ------- 4 Pool ------- # 
start_time = time.time()
pool = ThreadPool(4) 
results = pool.map(requests.get, urls)
print '4 Pool Done! Time taken: {}'.format(time.time() - start_time)
# # ------- 8 Pool ------- # 
start_time = time.time()
pool = ThreadPool(8) 
results = pool.map(requests.get, urls)
print '8 Pool Done! Time taken: {}'.format(time.time() - start_time)
# # ------- 13 Pool ------- # 
start_time = time.time()
pool = ThreadPool(13) 
results = pool.map(requests.get, urls)
print '13 Pool Done! Time taken: {}'.format(time.time() - start_time)
# # ------- 16 Pool ------- # 
start_time = time.time()
pool = ThreadPool(16) 
results = pool.map(requests.get, urls)
print '16 Pool Done! Time taken: {}'.format(time.time() - start_time)
# # ------- 19 Pool ------- # 
start_time = time.time()
pool = ThreadPool(19) 
results = pool.map(requests.get, urls)
print '19 Pool Done! Time taken: {}'.format(time.time() - start_time)