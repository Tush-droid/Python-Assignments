def Factotrial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact


def main():
    ret=Factotrial(int(input("Enter Value :")))
    print("factorial is:",ret)


if __name__=="__main__":
    main()

