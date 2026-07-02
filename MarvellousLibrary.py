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