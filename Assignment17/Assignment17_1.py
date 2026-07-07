from ArithmeticModule import Add,Sub,mul,div

print("-------------Welcome to digital calculator--------------"*100)

operation=int(input("Enter operation to perform \n 1.Add\n 2.subtraction \n3.Multiplication \n4 divison"))

if(operation==1):
    n1=int(input("Enter Number 1 :"))
    n2= int (input("Enter Number 2 :"))
    addtion=Add(n1,n2)
    print("Addition is :",addtion)
elif(operation==2):
    n1=int(input("Enter Number 1 :"))
    n2= int (input("Enter Number 2 :"))
    addtion=Sub(n1,n2)
    print("Addition is :",addtion)
elif(operation==3):
    n1=int(input("Enter Number 1 :"))
    n2= int (input("Enter Number 2 :"))
    addtion=mul(n1,n2)
    print("Addition is :",addtion)

elif(operation==4):
    n1=int(input("Enter Number 1 :"))
    n2= int (input("Enter Number 2 :"))
    ret=div(n1,n2)
    print("Div is :",ret)
else:print("Invalid input")
