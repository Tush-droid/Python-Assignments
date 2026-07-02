
#Code 1
def Display():
    print("Jay Ganesh...!")


Display()


#code2

def ChkGreater(n1,n2):
    if(n1>n2):
        print("greater num is :",n1)
    elif(n2>n1):
        print("greater num is :",n2)
    else:
        print("both are equal")

ChkGreater(20,40)

#code for printing square 

def SquareNumber(n):
    squ=n*n
    print("Square of Given Number is :",squ)

SquareNumber(10)

#code4 cube

def CubeNumber(no1):
    Cube=no1*no1*no1
    print("Cube of Given Number is :",Cube)

CubeNumber(10)

#code 5
def DivCheck(num):
    if(num%5==0):
        print("Number is Divisible by 5")
    elif(num%3==0):
        print("Number is divisible by 3")
    else:
        print("number is not divisible by 5 and 3")

DivCheck(25)