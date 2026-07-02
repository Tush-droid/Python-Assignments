#Accept :  multiple Parameter
#Return :  multiple values

def Marvellous(value1,value2):
    print("Inside MArvellous :" , value1,value2)
    return 21,51
def main():
    ret1,ret2=Marvellous(10,11)
    print("return is :" , ret1,ret2)


if __name__=="__main__":
    main()