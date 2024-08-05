a, b = 0, 1
sum = 0
while b <= 100:
    if b % 2 == 0:
        sum += b
    a, b = b, a + b
print("Sum of even-valued Fibonacci numbers until 100:", sum)