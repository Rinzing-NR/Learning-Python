n=int(input("Enter number\n"))
c=0
for i in range(2,n):
    if(n%i==0):
        c+=1
if(c==0):
    print("Prime")
else:
    print("Not Prime")