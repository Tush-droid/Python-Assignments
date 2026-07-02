from Marvellous import Substraction,Addition

def main():
    print("enter first number :")
    value1=int(input())

    print("Enter second number :")
    value2=int(input())

   
    result=Addition(value1,value2)
    result=Substraction(value1,value2)


    print("Substraction is ",result)

if(__name__=="__main__"):
    main()

