#  2. Christmas tree 

# Ask user to enter the height of the tree 

# Then Print the tree: Ex. height == 3 

# The printout would be: 

#   * 

#  *** 

# ***** 

# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

h = float(input("The height of the tree is: "))
h = int(h)

# FIXME Not the right code for this exercise
for n in range(30):
    if n%5 == 0 and n%7 == 0:
        print("FizzBuzz")
    elif n%5 == 0:
        print("Fizz")
    elif n%7 == 0:
        print("Buzz")
    else:
        print(n)