a=int(input("Enter 1st number\n"))
b=int(input("Enter 2nd number\n"))
hcf=1
for i in range(1,a+1 and b+1):
    if(a%i==0 and b%i==0):
        hcf=i
lcm=a*b/hcf
print("HCF\tLCM\n",hcf,"\t",lcm)