#Accept :  multiple Parameter
#Return :  multiple values

def Bigbazar():
    print("inside big b")

    def amul():
        print("inside amul ice cream")




def main():
  Bigbazar()#no error
  amul()#error
  Bigbazar.amul()#Error
  
    


if __name__=="__main__":
    main()