numbers = input("Enter a list of integers (space-separated): ").split()
distinct_pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if int(numbers[i]) * int(numbers[j]) % 2 != 0:
            distinct_pairs.append((int(numbers[i]), int(numbers[j])))
print("Distinct pairs with odd product:")
for pair in distinct_pairs:
    print(pair)