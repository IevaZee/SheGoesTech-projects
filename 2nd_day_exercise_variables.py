my_name = "Ieva"
print(type(my_name))
print(my_name)
my_num = 30
print(type(my_num))

a = 42
b = 42
c = 43
print(id(a))
print(id(a), id(b), id(c), id(my_num))
print(id(c)-id(a))

print(a, b, my_num)
b = 9001
c = 9_000
print(a, b, c, my_num)
print(a, b, c, my_num, sep="\n")
print(a, b, c, my_num, sep="\n***\n")

c = c + 5000
print(c)
c += 10_000
print(c)

c = c + 3.14
print(c, type(c))

c = c - 3.14
print(c, type(c))

c = int(c)
print(c, type(c))

e = 2.71828
e_rounded = round(e)
print(e_rounded, type(e_rounded))
e_rounded_to_2 = round(e, 2)
print(e_rounded_to_2, type(e_rounded_to_2))

my_str = "888.67"
my_float = float(my_str)
my_int = int(my_float)
print(my_str, my_float, my_int)

import datetime
print("Today is", datetime.datetime.now())
print("The year is", datetime.datetime.now().year)

my_name_exercise = input("What is your name? ")
print(f"That is a nice name {my_name_exercise}")

# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: 
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
username = input("What is your username? ")
print("How old are you " + username + "? ")
age = input("How old are you " + username + "? ")
years_until_100 = int(100) - age
print("You will be hundred years old in " + years_until_100 + " 🙂")