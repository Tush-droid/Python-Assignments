def Addition(No1,No2):
    ans=0
    ans=No1+No2
    return ans

def main():
    print("enter first number :")
    value1=int(input())

    print("Enter second number :")
    value2=int(input())

    result=Addition(value1,value2)

    print("Addition is ",result)

if(__name__=="__main__"):
    main()

