str=input("Enter a string")
str1=''
for i in str:
    str1= i+str1
if(str1==str):
    print("Palindrome")
else:
    print("Not Palindrome")