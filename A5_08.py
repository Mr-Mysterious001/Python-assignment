my_tuple = ()
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    element = input("Enter element {}: ".format(i + 1))
    my_tuple += (element,)
print("Tuple:", my_tuple)