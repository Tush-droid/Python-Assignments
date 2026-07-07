def retDigitCount(no):

    sum=0
    while(no>0):
        rem=no%10
        sum=rem+sum
        no=no//10
    print("Digit Count is :",sum)


retDigitCount(45)
