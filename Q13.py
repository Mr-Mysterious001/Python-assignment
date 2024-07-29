a=int(input("Enter a number"))
b=int(input("Enter a number"))
r=1
if(b>a):
    a,b=b,a
while(r!=0):
    r=a%b
    a=b
    b=r
print(a)
