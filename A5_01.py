numbers = [5, 2, 9, 1, 7]

if len(numbers) == 0:
    max_num = None
    min_num = None
else:
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

print("Maximum number:", max_num)
print("Minimum number:", min_num)
