
Addition = lambda No1,No2: No1+No2
CheckEven =lambda no : (no%2==0)

Increment = lambda no: no+1

#writing our own filter ,map ,reduce

def Filterx(Task,Elements):  #filter inner functionality

    Result=[]
    for no in Elements:
        ret=Task(no)
        if(ret==True):
            Result.append(no)
    return Result

def Mapx(Task,Elements):
    result=[]
    for no in Elements:
        ret=Task(no)#increment operation for no
        result.append(ret)
    return result

def reducex(Task,Elements):
    sum=0
    for no in Elements:
        sum=Task(sum,no)
    return sum






def main():
    Data=[12,32,4,15,16,20]

    print("Input data is",Data)

    FData=list(Filterx(CheckEven,Data))#passing another function as parameter 00functional prgm
    print("Data after filter ",FData)

    MData=list(Mapx(Increment,FData))
    print(MData)

    RData= reducex(Addition,MData)
    print(RData)



if __name__== "__main__":
    main()