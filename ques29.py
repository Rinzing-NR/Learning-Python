n=int(input("Enter number\n"))
cpy=n
sum=0
while n > 0:
    r=(int)(n%10)
    sum=sum*10+r
    n=(int)(n/10)
if(sum==cpy):
    print("Palindrome")
else:
    print("Not Palindrome")