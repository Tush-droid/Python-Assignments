from functools import reduce
#code1 map square numbers

def Square(no):
    return no*no


def C1():
    Data=[12,32,4,15,16,20]

    MData=(list(map(Square,Data)))

    print(MData)

C1()

#CODE 2 for filter

def CheckEven(no):
    return (no%2==0)

def C2():
    Data=[12,32,4,15,16,20]
    FData=list(filter(CheckEven,Data))
    print(FData)

C2()

#code 3 for odd check

def OddCheck(no1):
    return(no1%2!=0)

def C3():
    Data=[12,32,4,15,16,20]
    FData=list(filter(OddCheck,Data))
    print(FData)

C3()

#code 4 reduce

Add= lambda no1,no2:no1+no2


def C4():
    Data=[12,32,4,15,16,20]
    MData=reduce(Add,Data)
    print(MData)

C4()

# code 5 
MaxReturn= lambda no1,no2:max(no1,no2)

def C5():
    Data=[12,32,4,15,16,20]
    MData=reduce(MaxReturn,Data)
    print(MData)


C5()

#CODE 6

MinReturn= lambda no1,no2:min(no1,no2)

def C6():
    Data=[12,32,4,15,16,20]
    MData=reduce(MinReturn,Data)
    print(MData)


C6()

#code 7

fiveLetterString= lambda Str1 :(len(Str1)>5)
def C7():
    no_of_strings=int(input("Enter Number of strings"))
    Strings=[]
    for i in range (no_of_strings):
        strname=input("Enter String : ")
        Strings.append(strname)
    Fdata=list(filter(fiveLetterString,Strings))
    print(f"Strings greater that 5 characters are :{Fdata}")

C7()

#code 8


Divby3and5= lambda No:(No%5==0 and No%3==0)

def C8():
    Data=[12,32,4,15,16,20,23,30]
    Fdata= list(filter(Divby3and5,Data))
    print(f"Elements That are divide by 3 and 5 are {Fdata}")

C8()

#code 9 

def product(no1,no2):
    return no1*no2

def C9():
    Data=[12,32,4,15,16,20,23,30]
    Result= reduce(product,Data)
    print(f"Product of given list is :{Result}")

C9()

#code10
CountEven = lambda no :(no%2==0)
def C10():
    Data=[12,32,4,15,16,20,23,30]
    Result= list(filter(CountEven,Data))
    count=len(Result)
    print("Count of Even Numbers is :",count)
  

C10()




    














