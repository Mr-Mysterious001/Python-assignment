n=(input("Enter a number"))
l=len(n)
n=int(n)
n1=n
s=0
while(n1!=0):
    s=s+(n1%10)**l
    n1=int(n1/10)
if(n==s):
    print("Armstrong")
else:    
    print("Not Armstrong")