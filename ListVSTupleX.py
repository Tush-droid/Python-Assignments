#                      List         Tuple
#----------------------------------------------------------
#ordered                y              y
#Indexed                y              y
#MUtuable               y              n
#heterogeneous          y              y
#----------------------------------------------------------

def main():
   Data1=[10,3.14,True,"pune"] #list
   Data2=(10,3.14,True,"pune") #Tuple

   print(Data1)
   print(Data2)
   
   print(id(Data1))
   print(id(Data2))

   print(Data1[0])
   print(Data2[0])

if __name__=="__main__":
    main()