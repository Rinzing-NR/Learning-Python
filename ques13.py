units=int(input("Enter units\n"))
if(units<=100):
    ch=0.8*units
elif(units>100 and units<=200):
    ch=0.8*100+((units-100)*1)
else:
    ch=0.8*100+1*100+((units-200)*1.25)
print("Charge=",ch+50)