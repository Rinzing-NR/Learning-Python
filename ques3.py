basic=int(input("Enter basic salary\n"))
da=10/100*basic
hra=15/100*basic
fa=12.55/100*basic
pf=8.75/100*basic
gross=da+hra+basic+fa
net=gross-pf
anet=net*12
print("DA\t\tHRA\t\tFA\t\tPF\t\tGross\t\tNet\t\tAnet\n",da,"\t",hra,"\t",fa,"\t",pf,"\t",gross,"\t",net,"\t",anet)