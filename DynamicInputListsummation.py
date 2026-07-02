def Summation(Data):
    sum=0
    for no in Data:
        sum=sum+no
    return sum

def main():
    size=0
    arr=list()
    print("Enter elements for list")
    size=int(input())

    print("Enter the Elements")
    for i in range(size):
        no=int(input())
        arr.append(no)

    ret=Summation(arr)
    print(ret)


   

if __name__=="__main__":
    main()

