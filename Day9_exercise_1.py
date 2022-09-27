# 1. Min, Avg, Max

# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, and the largest value in the string, respectively.

# Example:

# get_min_avg_max ([0,10,1,9]) -> (0,5,10)

# the incoming sequence can be a tuple or a list with numeric values.



def get_min_avg_max(sequence):
    if type(sequence) != list:
        sequence = list(sequence)
    mini = min(sequence)
    maxi = max(sequence)
    aver = sum(sequence)/len(sequence)
    return mini, aver, maxi


print(get_min_avg_max([0,10,1,9]))