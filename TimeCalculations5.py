import time

def Factotrial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact


def main():
    Value=(int(input("Enter Value :")))
    start_time=time.perf_counter()
    ret=Factotrial(Value)
    end_time=time.perf_counter()
    print(f"Time Required is {end_time-start_time:.5f} seconds")
    print(f"factorial of {Value} is {ret}")


if __name__=="__main__":
    main()

