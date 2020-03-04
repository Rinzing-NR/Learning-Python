sale=int(input("Enter sale\n"))
if(sale>=100000):
    com=25/100*sale
elif(x>=80000 and x<100000):
    com=22.5/100*sale
elif(x>=60000 and x<80000):
    com=20/100*sale
elif(x>=40000 and x<60000):
    com=15/100*sale
else:
    com=12.5/100*sale
print("Commission=",com)