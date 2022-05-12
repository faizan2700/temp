from tasks3 import add, multiply
from tasks3 import REDIS_BACKEND 
'''
result = add.delay() 
print(result.ready())
while True:
    print(result.status) 
    if 'SUCCESS' in result.status:
        break 
print(result.result) 
'''

multiply.delay()
add.delay()
