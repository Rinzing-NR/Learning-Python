inc=int(input("Enter income\n"))
if(inc<=50000):
    tax=0
elif(inc>50000 and inc<=60000):
    tax=10/100*(inc-50000)
elif(inc>60000 and inc<=150000):
    tax=1000+(20/100*(inc-60000))
else:
    tax=19000+(30/100*(inc-150000))
print("Tax=",tax)