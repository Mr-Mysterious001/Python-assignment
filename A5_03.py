list1 = input("Enter values for list 1 separated by comma: ").split(sep=',')
list2 = input("Enter values for list 2 separated by comma: ").split(sep=',')
union = list1
for element in list2:
    if element not in union:
        union.append(element)
print("Union of the two lists:", union)