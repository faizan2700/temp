import time 
from datetime import datetime 
import threading 

def countdown(count):
    while(count >= 0):
        print("from {}=> Count down: {}".format(threading.current_thread().name, count)) 
        count -= 1
        time.sleep(1) 

def countup(count):
    cur_count = 0
    while(cur_count < count):
        print('from {}=> Count up: {}'.format(threading.current_thread().name, cur_count+1))
        cur_count += 1
        time.sleep(1)
    return
cur_time = datetime.now()
t1 = threading.Thread(name="countdown", args=(10,), target=countdown)
t1.start()
t2 = threading.Thread(name="countup", args=(10,), target=countup)
t2.start()
print('Party time!') 
t1.join()
t2.join()
total_time = datetime.now() - cur_time
print(total_time) 