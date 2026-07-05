import time,threading

def SumEven(No):
    print("TID of this SUmEVEn thread is ",threading.get_ident())
    

def SumOdd(No):
     print("TID of this SumODD thread is ",threading.get_ident())




    

def main():
    print("TID of this Main thread is ",threading.get_ident())
    S_time=time.perf_counter()
   # SumEven(1000000000)
    tobj=threading.Thread(target=SumEven,args=(100000000,))
   
   # SumOdd(1000000000)
    tobj2=threading.Thread(target=SumOdd,args=(10000000,))
    tobj.start()
    tobj2.start()
    tobj.join()
    tobj2.join()
    E_time=time.perf_counter()
    print(f"Time Required to for it is{E_time-S_time:.4f} ")
    


if __name__=="__main__":
    main()