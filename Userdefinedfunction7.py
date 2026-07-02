#Accept :  multiple Parameter
#Return :  multiple values


def Calculation(no1,no2):
    Mul=no1*no2
    Div=no1/no2
    return Mul,Div



def main():
    val1=int(input("Enter Num 1:"))
    val2=int(input("Enter num 2:"))

    ret1,ret2=Calculation(val1,val2)
    print("Multiplication is ",ret1)
    print("Division is ",ret2)
  
    


if __name__=="__main__":
    main()