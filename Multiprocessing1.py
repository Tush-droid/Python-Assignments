import time
import multiprocessing

def SumEven(No):
    sum=0
    for i in range(2,No,2):
        sum=sum+i
    print("Sumof Evens:",sum)
    

def SumOdd(No):
    sum=0
    for i in range(1,No,2):
        sum=sum+i
    print("Sumof Odds:",sum)




    

def main():
    S_time=time.perf_counter()
   # SumEven(1000000000)
    tobj=multiprocessing.process(target=SumEven,args=(100000000,))
   
   # SumOdd(1000000000)
    tobj2=multiprocessing.process(target=SumOdd,args=(10000000,))
    tobj.start()
    tobj2.start()
    tobj.join()
    tobj2.join()
    E_time=time.perf_counter()
    print(f"Time Required to for it is{E_time-S_time:.4f} ")
    


if __name__=="__main__":
    main()