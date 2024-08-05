n=int(input("Enter a number"))
n1=n
s=0
while(n1!=0):
    s=s+(n1%10)**3
    n1=int(n1/10)
if(n==s):
    print("Armstrong")
else:    
    print("Not Armstrong")