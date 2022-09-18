#  2. Christmas tree 

# Ask user to enter the height of the tree 

# Then Print the tree: Ex. height == 3 

# The printout would be: 

#   * 

#  *** 

# ***** 

# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

h = int(input("Enter the height of the tree: "))
asterisks = 1
while h > 0:
    print(" " * (h-1) + "*" * asterisks)
    h -= 1
    asterisks += 2