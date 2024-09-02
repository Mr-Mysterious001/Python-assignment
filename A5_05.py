list1=input("Enter values for list 1 separated by comma").split(sep=',')
list2=input("Enter values for list 2 separated by comma").split(sep=',')
union=[]
max_num = max(len(list1),len(list2))
for i in range(0,max_num):
    if len(list2)>len(list1):
        if list2[i] not in list1:
            union.append(list2[i])
    else:
        if list1[i] not in list2:
            union.append(list1[i])      
print(union)