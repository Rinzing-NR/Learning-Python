sale=int(input("Enter sale\n"))
if(sale<=5000):
    com=5/100*sale
elif(sale>5000 and sale<=10000):
    com=10/100*sale
elif(sale>10000 and sale<=20000):
    com=20/100*sale
else:
    com=30/100*sale
print("Commission=",com)