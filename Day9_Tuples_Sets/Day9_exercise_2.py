# 2. Common Elements



# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.

# get_common_elements(seq1, seq2, seq3)

# Example:

# get_common_elements("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element 

# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)

# 2. b For those with some experience 

# BONUS:  make a function that can handle an arbitrary number of input sequences
# so function which takes any number of sequences and returns a tuple with common elements
# get_common_elements(seq1, seq2, seq3, seq4, seq5, seq6, seq7) etc :), so just like print takes any number of values


# SOLUTION for 2A:

# def get_common_elements(seq1, seq2, seq3):
#     seq1 = set(seq1)
#     seq2 = set(seq2)
#     seq3 = set(seq3)
#     return tuple(seq1&seq2&seq3)


# print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))



# SOLUTION for 2B:

def get_common_elements(*args):
    if len(args) == 0:
        return tuple()
    return tuple((set(args[0]).intersection(*args[1:])))


print(get_common_elements("abc", ['a', 'b'], ('b', 'a', 'c'), 'Ievas ābols', 'kabacis'))