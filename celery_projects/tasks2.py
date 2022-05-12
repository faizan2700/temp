import threading 
import time 
import random 

global queue 
queue = list()
MAX_ITEMS = 10 

condition = threading.Condition() 

class ProducerThread(threading.Thread):
    def run(self):
        numbers = range(5) 

        while True:
            condition.acquire()
            if len(queue) == MAX_ITEMS:
                print('Queue is full, producer is waiting...') 
                condition.wait() 
                print('Spae in queue, Consumer notified producer...')
            number = random.choice(numbers) 
            queue.append(number) 
            print('Produced {}'.format(number)) 
            condition.notify() 
            condition.release() 
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    def run(self):
        global queue 
        while True:
            condition.acquire() 
            if not queue:
                print('Nothing in queue') 
                condition.wait() 
                print('Producer added something, notified to consumer...') 
            number = queue.pop(0) 
            print('Consumed {}'.format(number)) 
            condition.notify()
            condition.release() 
            time.sleep(random.random())

producer = ProducerThread()
consumer = ConsumerThread()

producer.start()
consumer.start()
print('parent exiting...') 

while True:
    time.sleep(10) 
