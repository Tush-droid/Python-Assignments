from functools import reduce


Addition = lambda No1,No2: No1+No2
CheckEven =lambda no : (no%2==0)

Increment = lambda no: no+1

def main():
    Data=[12,32,4,15,16,20]

    print("Input data is",Data)

    FData=list(filter(CheckEven,Data))#passing another function as parameter 00functional prgm
    print("Data after filter ",FData)

    MData=list(map(Increment,FData))
    print(MData)

    RData= reduce(Addition,MData)
    print(RData)



if __name__== "__main__":
    main()