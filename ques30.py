import math

n=int(input("Enter number\n"))
cpy=n
sum=0
while n > 0:
    r=(int)(n%10)
    sum=sum+math.pow(r,3)
    n=(int)(n/10)
if(sum==cpy):
    print("Armstrong")
else:
    print("Not Armstrong")