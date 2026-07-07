n= int(input("Enter Number of elements in the list"))
list1=[]
for i in range(n):
    var=int(input("Enter element"))
    list1.append(var)

n2=int(input("Enter number to check frequnecy"))
freq=0
for no in list1:
    if(no==n2):
        freq=freq+1
    

print(f" frequency of {n2} is {freq}")
    
