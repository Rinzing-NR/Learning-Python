n=int(input("Enter a number\n"))
a=0
b=1
sum=0
while sum<n:
    if(sum%2==0):
        print(sum," ")
    sum=a+b
    b=a
    a=sum