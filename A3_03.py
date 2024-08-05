a = int(input("Enter the first positive number: "))
b = int(input("Enter the second positive number: "))
max = max(a, b)
lcm = max
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += max
print("The LCM of", a, "and", b, "is", lcm)