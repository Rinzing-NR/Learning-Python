calls=int(input("Enter calls\n"))
if(calls<=50):
    ch=0
elif(calls>50 and calls<=150):
    ch=50*0+((calls-50)*1)
elif(calls>150 and calls<=350):
    ch=50*0+100*1+((calls-150)*0.9)
else:
    ch=50*0+100*1+200*0.9+((calls-350)*0.8)
print("Charge=",ch+180)