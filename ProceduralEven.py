def CheckEven(No):
    if(No%2==0):
        print("Even")
    else:
        print("Odd")

def main():
    Value=int(input("Enter number:"))
    CheckEven(Value)


if __name__=="__main__":
    main()