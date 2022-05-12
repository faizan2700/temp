from celery import Celery  
from celery.exceptions import SoftTimeLimitExceeded

from datetime import timedelta 

import time 
import random 

REDIS_BROKER_URL = 'redis://localhost:6379/0'
REDIS_BACKEND = 'redis://localhost:6379/0'
app = Celery('tasks', backend=REDIS_BACKEND, broker=REDIS_BROKER_URL) 

@app.task(name='tasks.add')
def add():
    time.sleep(4)
    x = int(100*random.random())
    y = int(100*random.random())
    print('{} + {} = {}'.format(x, y, x+y)) 
    return x+y 

def backoff(attempts):
    '''
    instantly, 1, 2, 4, 8, 16, 32....
    '''
    return 2 ** attempts 

@app.task(name='tasks.multiply', bind=True, max_retries=4, soft_time_limit=5) 
def multiply(self):
    try:
        time.sleep(5)
        x = int('s') 
    except Exception as e:
        print('exception happened!!!') 
        raise self.retry(exc=e, countdown=backoff(self.request.retries))
    except SoftTimeLimitExceeded as e:
        raise self.retry(exc=e, countdown=backoff(self.request.retries))

