
import time 
import threading 
import Queue 
import requests 

class Consumer(threading.Thread): 
    def __init__(self, queue): 
        threading.Thread.__init__(self)
        self._queue = queue 

    def run(self):
        while True: 
            content = self._queue.get() 
            if isinstance(content, str) and content == 'quit':
                break
            response = requests.get(content)
            print response.status_code
        print 'Bye byes!'


def Producer():
    urls = [
        'http://www.baidu.com', 'http://www.baidu.com',
        'http://www.baidu.com', 'http://www.baidu.com',
        # etc.. 
    ]
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, 4)
    start_time = time.time()

    # Add the urls to process
    for url in urls: 
        queue.put(url)  
    # Add the poison pillv
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()

    print 'Done! Time taken: {}'.format(time.time() - start_time)

def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start() 
        workers.append(worker)
    return workers

if __name__ == '__main__':
    Producer()
    start_time2 = time.time()
    for i in range(4):
        response = requests.get('http://www.baidu.com')
        print response.status_code
    print 'Done! Time taken: {}'.format(time.time() - start_time2)