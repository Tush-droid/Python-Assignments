def VowelCheck(x):
    if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
        print("Vowel")
    else:
        print("Constant")

VowelCheck("i")

def FactorPrinter(no):
     for i in range(1,no+1):
         if(no%i==0):
             print(i," ")


FactorPrinter(56)


def Calculator(n1,n2):
    return n1+n2,n1-n2,n1*n2,n1/n2

no1=int(input("Enter Num 1 :"))
no2=int(input("Enter Num 2 :"))

add,sub,mul,div=Calculator(no1,no2)
print("addotion is",add)
print("Subtraction is :",sub)
print("multiplication is:",mul)
print("div is:",div)


def NumPrinting(no3):
    for i in range(1,no3):
        print(i)

NumPrinting(int(input("Enter num : ")))

def NumPrintingReverse(no4):
    print(no4)
    while(no4>0):
        no4=no4-1
        print(no4,",")

NumPrintingReverse(int(input("Enter num : ")))



