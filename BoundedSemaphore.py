from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import BoundedSemaphore
from time import sleep 

N = 8

def task(common, tid, bounded_sem):
    
    a = 0
    for i in range(100):
        print(f"{tid}−{i}: Non−critical Section")
        a += 1
        print(f"{tid}−{i}: End of non−critical Section")
        bounded_sem.acquire()
        print(f"{tid}−{i}: Critical section")
        v = common.value + 1
        print(f"{tid}−{i}: Inside critical section")
        common.value = v
        sleep(0.1)
        print(f"{tid}−{i}: End of critical section")
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
