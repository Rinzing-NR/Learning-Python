days=int(input("Enter days\n"))
if(days<=7):
    ch=0.2*days
elif(days>7 and days<=14):
    ch=0.3*days
elif(days>14 and days<=21):
    ch=0.4*days
else:
    ch=0.5*days
print("Fine=",ch)