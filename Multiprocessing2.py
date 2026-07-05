import time
import multiprocessing
import os

def SumEven(No):
    print(f"PID of sumeven :{os.getpid()} and parent ID :{os.getppid()} ")

    sum=0
    for i in range(2,No,2):
        sum=sum+i
    print("Sumof Evens:",sum)
    

def SumOdd(No):
    print(f"PID of sumodd:{os.getpid()} and parent ID :{os.getppid()} ")
    sum=0
    for i in range(1,No,2):
        sum=sum+i
    print("Sumof Odds:",sum)




    

def main():
    S_time=time.perf_counter()
    print(f"PID of main :{os.getpid()} and parent ID :{os.getppid()} ")
   # SumEven(1000000000)
    t1 = multiprocessing.Process(target=SumEven,args=(1000,))
   
   # SumOdd(1000000000)
    t2 = multiprocessing.Process(target=SumOdd,args=(1000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    E_time=time.perf_counter()
    print(f"Time Required to for it is{E_time-S_time:.4f} ")
    


if __name__=="__main__":
    main()