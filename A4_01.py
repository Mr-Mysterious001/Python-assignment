str=input("Enter a sentence ")
str=str.lower()
v=0
for ch in str:
    if (ch=='a') or (ch=='e') or (ch=='i') or (ch=='o') or (ch=='u'):
        v+=1
print('No. of vowels: ', v)