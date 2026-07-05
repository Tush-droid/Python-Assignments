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
    SumEven(1000000000)
    SumOdd(1000000000)
    


if __name__=="__main__":
    main()