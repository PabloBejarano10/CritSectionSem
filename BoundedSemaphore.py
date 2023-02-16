from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import BoundedSemaphore
from time import sleep 
from random import random

N = 8

def task(common, tid, bounded_sem):
    for i in range(10):
        print(f"{tid}−{i}: Non−critical Section", flush = True)
        sleep(random())
        print(f"{tid}−{i}: End of non−critical Section", flush = True)
        bounded_sem.acquire()
        print(f"{tid}−{i}: Critical section", flush = True)
        v = common.value + 1
        print(f"{tid}−{i}: Inside critical section", flush = True)
        sleep(random())
        common.value = v
        print(f"{tid}−{i}: End of critical section", flush = True)
        bounded_sem.release()
        
def main():
    bounded_sem  = BoundedSemaphore(1)
    lp = []
    common = Value("i", 0)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, bounded_sem)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")
if __name__ == "__main__":
    main()
