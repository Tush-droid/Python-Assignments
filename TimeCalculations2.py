def Factotrial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact


def main():
    Value=(int(input("Enter Value :")))
    ret=Factotrial(Value)
    print(f"factorial of {Value} is {ret}")


if __name__=="__main__":
    main()

