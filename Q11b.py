a=0
b=10
for i in range(1,6):
    for k in range(1,i):
        print(' ', end='')
        a=a+1
    for j in range(1,b):
        print("*",end='')
    b=b-2
    print()
