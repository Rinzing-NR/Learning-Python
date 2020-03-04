n=int(input("Enter limit\n"))
for i in range(1,n+1):
    a=0
    for j in range(1,n+1):
        if j>=i:
            print(a,end="")
            a=a+3
        else:
            print(" ",end="")
    print("")