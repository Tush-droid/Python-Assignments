Square = lambda num1 : num1*num1

def SquareFunction(no1):
    ret=Square(no1)
    print("sqaare is :",ret)

SquareFunction(12)


#code 2

Cube= lambda num2 : num2*num2*num2

def Cubefunction(no2):
    ret2= Cube(no2)
    print("Cube is: ",ret2)

Cubefunction(3)

#
Max = lambda no3,no4 : max(no3,no4)

def Maxfunction(num3,num4):
    ret=Max(num3,num4)
    print("Maximum number is :",ret)

Maxfunction(11,21)


#

Min = lambda no5,no6 : min(no5,no6)

def MinFunction(num5,num6):
    ret1=Min(num5,num6)
    print("Minimum is :",ret1)


MinFunction(11,21)


Even = lambda no7: (no7%2==0)

def TrueCheck(num7):
    ret4= Even(num7)
    print(ret4)

TrueCheck(5)


#

Odd = lambda no8: (no8%2!=0)

def OddCheck(num8):
    ret=Odd(num8)
    if(ret==True):
        print("Number is Odd")
    else:
        print("Number is Even")




#div by 5

DivCheck = lambda num9 : (num9%5==0)

def DivCheck5Function(no9):
    ret=DivCheck(no9)
    if(ret==True):
        print(f"Number {no9} is divisible by 5")
    else:
        print("number is not divisible by 5")

DivCheck5Function(50)

Add = lambda n10,n11 : n10+n11


def RetAdd(no10,no11):
    ret=Add(no10,no11)
    print("addition is :",ret)


RetAdd(11,21)

# multiplication


Multiply = lambda n10,n11 : n10*n11


def RetMul(no10,no11):
    ret=Multiply(no10,no11)
    print("Multiplication is :",ret)


RetMul(11,21)


# max for 3 nums

Maxfor = lambda n1,n2,n3:max(n1,n2,n3)

def Maxofthree(n12,n13,n14):
    ret=Maxfor(n12,n13,n14)
    print("Maximum is :",ret)

Maxofthree(4,5,1)


