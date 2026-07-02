#                      List         Tuple
#----------------------------------------------------------
#ordered                y              y
#Indexed                y              y
#MUtuable               y              n
#----------------------------------------------------------

def main():
   Data1=[10,20,30,40] #list
   Data2=(10,20,30,40) #Tuple

   print(Data1)
   print(Data2)
   
   print(id(Data1))
   print(id(Data2))

   print(Data1[0])
   print(Data2[0])

if __name__=="__main__":
    main()