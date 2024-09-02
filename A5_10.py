tuple_nums = tuple(input("Enter comma-separated numbers: ").split(","))
unique_nums = []
for num in tuple_nums:
    if num not in unique_nums:
        unique_nums.append(num)
if unique_nums:
    for num in unique_nums:
        print(num)
