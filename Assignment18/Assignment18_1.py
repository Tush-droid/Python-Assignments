n= int(input("Enter Number of elements in the list"))
list1=[]
for i in range(n):
    var=int(input("Enter element"))
    list1.append(var)
sum=0
for no in list1:
    sum=sum+no


print(f"sum is :{sum}")


