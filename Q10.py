p=int(input("Enter principal amount"))
t=int(input("Enter time"))
if(p<200000):
    print((p*t*0.1)/100)
elif(p>200000 and p<1000000):
    print((p*t*0.12)/100)
else:
    print((p*t*0.15)/100)
