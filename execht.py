t=int(input())
for i in range(0,t+1):
    a=int(input())
    b=int(input())
    p=1
    c=0
    while p<a or p<b:
        if((a-1)%p == (b-1)%p):
            c+=1
        p+=1
    print(c)