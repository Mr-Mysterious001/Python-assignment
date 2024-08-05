num=0
prime=0
comp=0
while num!=-1:
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                comp+=1
                break
        else:
            prime+=1
print("Number of primes: ", prime)
print("Number of composites: ", comp)