n= int(input("Enter Number of elements in the list"))
list1=[]
for i in range(n):
    var=int(input("Enter element"))
    list1.append(var)

mini=min(list1)

print(f"Minimum is {mini}")