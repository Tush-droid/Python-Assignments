
#code1


def PrimeCheck(n):
    if n <= 1:
        print("Not Prime")
        

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
        

    print("Prime")

PrimeCheck(13)





def CountDigits(n3):
    temp=0

    while(n3>0):
    
        temp=temp+1
        n3=n3//10
    print("sum ",temp)

CountDigits(1234)











#code 2

def DigitSum(n3):
    temp=0

    while(n3>0):
    
        digit=n3%10
        temp=digit+temp
        n3=n3//10
    print("sum ",temp)

DigitSum(1234)












#code 3

def ReverseNUm(n4):
    rev=0
    
    while(n4>0):
    
        digit=n4%10
        rev=rev*10+digit
        n4=n4//10
    print(rev)    

    
ReverseNUm(12321)
#code 4

def PalindromeCheck(n4):
    rev=0
    temp=n4
    while(n4>0):
    
        digit=n4%10
        rev=rev*10+digit
        n4=n4//10
        
    if(rev==temp):
            print("Its palindrome number")
    else:
            print("NUmber is not palindrome")
    
PalindromeCheck(12321)
    