
CheckEven= lambda no :no%2==0

def main():
    Data=[12,32,4,15,23,67,16,20]

    print("Input data is",Data)

    FData=list(filter(CheckEven,Data))#passing another function as parameter 00functional prgm
    print("Data after filter ",FData)



if __name__== "__main__":
    main()