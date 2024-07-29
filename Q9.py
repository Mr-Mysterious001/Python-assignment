a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if(a>b):
    if(a>c):
        a,c=c,a
        if(a>b):
            a,b=b,a
    else:
        a,b=b,a
elif(a<b):
    if(b>c):
        b,c=c,b
        if(c>a):
            a,c=c,a
    else:
        b,a=a,b
else:
    print("Wrong Input")
print(a,b,c)
