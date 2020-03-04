n=int(input("Enter number\n"))
sum=0
while n > 0:
    r=(int)(n%10)
    sum=sum+r
    n=(int)(n/10)
print("Sum of digits=",sum)