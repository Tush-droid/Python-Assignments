def retDigitCount(no):

    digit=0
    while(no>0):
        no=no//10
        digit=digit+1
    print("Digit Count is :",digit)


retDigitCount
