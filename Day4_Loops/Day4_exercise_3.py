# 3. Primes Check if entered positive number is a prime number.

#  A prime number is a number that divides without remainder only by itself and 1.

# Hint: what numbers do we have to check?


num = int(input("Please enter a positive number: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number. It divides by {i}")
        break
else:
    if num == 1:
        print(f"{num} is not a prime number")
    if num > 1:
        print(f"{num} is a prime number")


# OR FLAG BASED APPROACH (used more than the first approach)

num = int(input("Please enter a positive number: "))
not_prime = False

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            not_prime = True
            break
if not_prime:
    print(f"{num} is not a prime number. It divides by {i}")
else:
    print(f"{num} is a prime number")