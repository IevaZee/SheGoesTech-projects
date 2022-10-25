# TODO
# put the imports first

# create a function that returns a list of random dice throws
# it should have two parameters
# - number of dice in each throw, default 4
# - number of throws, default 100


# even better would be a another function to which you give the list of dice throws and it 
# plots the histogram
# this function would have two parameters
# - the list of dice throws - no default
# - the name of the file to save the plot to - default - empty string
# if the file name is empty string, the plot should be shown on the screen

# use the first function to create a list of 1000 dice throws with 6 dice in each throw
# pass the result to 2nd function to plot the histogram and save it to a file
# BONUS: file name should have current date and time in it


# ideally you would then run them from main guard
# which means this file would be a module, that can be imported


import random
from matplotlib import pyplot as plt
from datetime import datetime
import os
os.chdir("C:\\Users\\ievaz\\OneDrive\\Documents\\SheGoesTech-projects\\Day14")


def get_dice_throws(number_of_dice=4, number_of_throws=100):
    dice_throws = []
    for n in range(number_of_throws):
        one_throw = 0
        for _ in range(number_of_dice):
            numb = random.randint(1,6)
            one_throw += numb
        dice_throws.append(one_throw)
    return dice_throws

dice_throw_list = get_dice_throws(6,1000)
# print(dice_throw_list)


def get_histogram(dice_throw_list, file_name=""):
    n_bins = (max(dice_throw_list)-min(dice_throw_list))
    n, bins, patches = plt.hist(dice_throw_list, n_bins, facecolor='g', rwidth=0.9)
    plt.xlabel("Total number on the dices")
    plt.ylabel("Occurrence")
    plt.title("Histogram of dice throws")
    if file_name:
        plt.savefig(file_name)  # TODO File name should have current date and time in it
    return plt.show()

my_histogram = get_histogram(dice_throw_list, "My_graph")


if __name__ == "__main__":
    dice_throw_list = get_dice_throws()
    my_histogram = get_histogram(dice_throw_list)