def FactAdd(no):
    sum=0

    for i in range(1,no+1):
        if(no%i==0):
            sum=sum+i
    print("Factorail sum is :",sum)


FactAdd(15)