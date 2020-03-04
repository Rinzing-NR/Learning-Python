import math

prep=int(input("Enter present population\n"))
n=int(input("Enter number of years\n"))
po=prep*math.pow(1.06,n)
print("Future Population=",po)