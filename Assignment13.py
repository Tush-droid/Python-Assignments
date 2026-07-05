def AreaOfRectangle(length, width):
    area = length * width
    return area

area1 = AreaOfRectangle(5, 10)
print("Area of Rectangle is:", area1)

def AreaOfCircle(radius):
    area = 3.14 * radius * radius
    return area

area2 = AreaOfCircle(5)
print("Area of Circle is:", area2)  

def checkPerfectNumber(num):
    divisorsum= 0
    for i in range(1, num):
        if num % i == 0:
            divisorsum =divisorsum + i
    if divisorsum == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is not a Perfect Number")

checkPerfectNumber(28)


def GraderDivider(marks):
    if(marks>100):
        print("invalid input")
    elif(marks<=100 and marks>=75):
        print("Distinction")
    elif(marks<75 and marks>=60):
        print("First Class")
    elif(marks<60 and marks>=50):
        print("Second Class")
    else:
        print("failed")

GraderDivider(int(input("Enter Marks")))


def BinaryConverter(Number):
    if Number==0:
         return 0;
    list=[]
    while(Number>0):
        var1=Number%2
        list.append(var1)
        Number=Number//2
    for item in reversed(list):
        print(item)
    
        
       
      
    
 #  b_string=bin(Number)
  # print(b_string)

BinaryConverter(34)    



