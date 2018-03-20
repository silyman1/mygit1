from multiprocessing import Process, Semaphore, Lock, Queue
import time
 
buffer = Queue(10)
empty = Semaphore(3)
full = Semaphore(0)
lock = Lock()
 
class Consumer(Process):
 
    def run(self):
        global buffer, empty, full, lock
        while True:
            print('1')
            full.acquire()
            print('2')
            lock.acquire()
            print('3')
            buffer.get()
            print('Consumer pop an element')
            time.sleep(1)
            lock.release()
            empty.release()
 
 
class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            empty.acquire()
            lock.acquire()
            buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            print('111')
            lock.release()
            print('222')
            full.release()
            print('3333')
 
 
if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    p.join()
    c.start()
    c.join()
    print 'Ended!'