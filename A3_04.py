lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

sum = 0

for i in range(lower, upper + 1):
    if i > 1:
        for j in range(2, i):
            if (i% j) == 0:
                break
        else:
            sum += i

print("Sum of prime numbers:", sum)