import threading 

counter_buffer = 0
list_buffer = []


global thread_list 
thread_list = []
counter_lock = threading.Lock() 

COUNTER_MAX = 100000

def consumer1_counter():
    global counter_buffer 
    global list_buffer
    for i in range(COUNTER_MAX):
        #counter_lock.acquire()
        #print(threading.current_thread().name) 
        counter_buffer += 1
        #counter_lock.release()

def consumer2_counter():
    global counter_buffer 
    global list_buffer 
    for i in range(COUNTER_MAX):
        #counter_lock.acquire()
        list_buffer.append(threading.current_thread().name)
        counter_buffer += 1 
        #counter_lock.release() 

def gen_thread(name):
    t = threading.Thread(target=consumer1_counter, name=name) 
    thread_list.append(t)

def main():
    for i in range(1000):
        gen_thread(str(i))
    for i in range(len(thread_list)):
        thread_list[i].start() 
    for i in range(len(thread_list)):
        thread_list[i].join()
    return

if __name__ == '__main__':
    main()
    print(counter_buffer) 
    #print(list_buffer[:1000009])
