units=float(input("Enter units\n"))
if(units<=100):
    ch=units*1
elif(units>100 and units<=200):
    ch=(100*1)+(units-100)*2
else:
    ch=(100*1)+(100*2)+((units-200)*3)
print("Charge=",ch)