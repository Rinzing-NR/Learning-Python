n=int(input("Enter a number\n"))
a=0
b=1
sum=0
for i in range(1,n+1):
    print(sum," ")
    sum=a+b
    b=a
    a=sum