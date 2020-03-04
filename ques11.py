x=int(input("Enter percentage\n"))
if(x>=75):
    print("Passed with star")
elif(x>=60 and x<75):
    print("1st division")
elif(x>=40 and x<60):
    print("2nd division")
else:
    print("Fail")