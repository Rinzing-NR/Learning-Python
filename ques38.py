n=int(input("Enter limit\n"))
x=int(input("Enter numerator\n"))
sum=0
for i in range(1,n+1):
    sum=sum+(x/i)
print("Sum=",sum)