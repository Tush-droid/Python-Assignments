print("--------------------------------TIcket software-------------------------------"*1000)

print("Enter Age")
Age=int(input())

if(Age<=5):
    print("No Charges Applied")
elif(Age>=5 and Age<=18):
    print("Your Ticket Prize is : 900")
elif(Age>=19 and Age<=40):
    print("Ticket Prize is :1200")
else:
    print("passsssehhh")