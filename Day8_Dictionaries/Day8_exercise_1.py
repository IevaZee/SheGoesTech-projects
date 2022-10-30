# # 1. What's the frequency?

# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.

# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 

# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included

#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile



# SOLUTION:
# Works correctly but is not optimal because it will take a lot of time (loop inside another loop)

# def get_char_count(text):
#     new_dict = {}
#     for char in text:
#         char_count = text.count(char)
#         new_dict[char]=char_count
#     return new_dict


# ANOTHER SOLUTION:
# Optimal because works much faster

def get_char_count(text):
    new_dict = {}
    for char in text:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict


# ANOTHER APPROACH:
# Using imported counter

from collections import Counter
my_counter = Counter("hubba bubba")
print(my_counter)
regular_dict = dict(my_counter)
print(regular_dict)

#TESTING:
print(get_char_count("hubba bubba"))
print(get_char_count("AbracadAbra"))