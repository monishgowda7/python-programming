import threading
import time

def worker(num):
    print(f"thread {num}:starting")
    time.sleep(4)
    print(f"thread {num}:finishing")
    
threads=[]
for i in range(1,4):
    thread=threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()
    
for thread in threads:  
    thread.join() 
        
        
# hey i will give some sentence in broken english.you have to fix it and tell me why they are wrong.if you find better sentence,suggest that too.are you ready 