from functools import reduce
n= int(input("Enter Number of elements in the list"))
list1=[]
for i in range(n):
    var=int(input("Enter element"))
    list1.append(var)

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


number = 17

fData=list(filter(isPrime,list1))
print(fData)

def add(no1,no2):
    return no1+no2

total_prime=reduce(add,fData)

print("total prime numbers are: ",total_prime)