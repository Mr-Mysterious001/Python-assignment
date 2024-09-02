tuple_data = tuple(input("Enter comma-separated numbers: ").split(","))
elements = []
counts = []
for element in tuple_data:
    if element in elements:
        index = elements.index(element)
        counts[index] += 1
    else:
        elements.append(element)
        counts.append(1)
print(elements)
print(counts)