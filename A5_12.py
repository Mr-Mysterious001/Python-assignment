numbers = tuple(input("Enter comma-separated numbers: ").split(","))
distinct_pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = int(numbers[i]) * int(numbers[j])
        if product % 2 == 0:
            distinct_pairs.append((numbers[i], numbers[j]))
print(distinct_pairs)