# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise
# https://github.com/ValRCS/Python_SheGoesTech_22/blob/main/Day_4_Loops/day4_exercise_3.py



# num_of_primes = int(input("How many primes do you want to find? "))
# n = 1000
# primes_list = []
# numbers = list(range(2,n))

# for number in numbers:
#     for i in range(2, int(number**0.5+1)):
#         if number % i == 0:
#             break
#     else:
#         primes_list.append(number)
#         if len(primes_list) == num_of_primes:
#             break
# print(primes_list)



# OR OTHER SOLUTION USING FUNCTIONS:

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5+1)):
        if number % i == 0:
            return False
    return True

def get_primes_list(prime_range=20, current=2):
    prime_list=[]
    counter=0
    while counter < prime_range:
        if is_prime(current):
            prime_list.append(current)
            counter+=1
        current+=1
    return prime_list

primes_20 = get_primes_list()
print(primes_20)