def TablePrinter(n):
    for i in range(1,11):
        print(i*n)

TablePrinter(5)

#code 2 natural number sum print

def SumofNaturalNumber(n2):
    sum=0
    for i in range(1,n2+1):
       sum=sum+i
    print(sum)

SumofNaturalNumber(5)


#code 3

def PrintFactorial(n3):
    fact=1
    for i in range(1,n3+1):
        fact=fact*i
    print(fact)

PrintFactorial(5)


#code4

def EvenPrinter(n4):
    for i in range(1,n4+1):
        if(i%2==0):
            print(i)


EvenPrinter(45)



#code5
def OddPrinter(n4):
    for i in range(1,n4+1):
        if(i%2!=0):
            print(i)


OddPrinter(45)
