str=input("Enter a sentence ")
str1=''
last=len(str)-1
for i in last-1:
    if(str[i]==str[last-1]):
        str1=str1+'*'
    else:
        str1=str1+str[i]
print(str1)