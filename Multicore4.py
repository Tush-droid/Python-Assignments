import time,multiprocessing,os
def SumCube(no):
    print("process is running with pid:",os.getpid())
    sum=0
    for i in range(1,no+1):
        sum=sum+(i**3)
    return sum






def main():
    Data=[1000000,2000000,3000000,4000000,5000000]

    start_time=time.perf_counter()
    result=[]
    pobj=multiprocessing.Pool()
    result=pobj.map(SumCube,Data)
    pobj.close()
    pobj.join()
    end_time=time.perf_counter()
    print("Result is ")
    print(result)
    print(f"Time required is :{end_time-start_time:.4f} ")

    


    ret=SumCube(5)
    print(f"result is {ret}")
    
if __name__ == "__main__":
    main()

