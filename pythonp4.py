import threading
import time

def funk1():
    
        for i in range(0,150):
            time.sleep(0.1)
            print(i)
            if i == 50:
                break

def funk2():
    
        for i in range(0,150):
            time.sleep(0.1)
            print(i)
            if i == 100:
                
                break
def funk3():
    
        for i in range(0,151):
            time.sleep(0.1)
            print(i)
            if i == 150:
                break
                

f1 = threading.Thread(target=funk1)
f2 = threading.Thread(target=funk2)
f3 = threading.Thread(target=funk3)

f1.start()
f2.start()
f3.start()
