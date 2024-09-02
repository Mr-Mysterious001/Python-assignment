str=input("Enter a sentence")+' '
str1=''
count=0
word=input("Enter a word")
for ch in str:
    if(ch==' '):
        if(str1==word):
            count+=1
        str1=''
    else:
        str1=str1+ch
print(count)