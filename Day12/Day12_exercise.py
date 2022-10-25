# Exercise
# read text from  sherlock_holmes_adventures.txt

import os
os.chdir("C:\\Users\\ievaz\\OneDrive\\Documents\\SheGoesTech-projects\\Day12")



# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len("sherlock_holmes_adventures.txt") -> 12305

# SOLUTION:

# def file_line_len(fpath):
#     with open(fpath, encoding="utf-8") as fstream:
#         lines = fstream.readlines()
#     return len(lines)

# ANOTHER SOLUTION - better for bigger files:

def file_line_len(fpath):
    file_len = 0
    with open(fpath, encoding="utf-8") as fstream:
        for _ in fstream:
            file_len += 1
    return file_len


# print(file_line_len("sherlock_holmes_adventures.txt"))


# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

# So we want to avoid/filter out those lines that contain whitespace

# PS preferably use encoding = "utf-8" when reading 

# SOLUTION:

def get_text_lines(fpath):
    with open(fpath, encoding="utf-8") as fstream:
        lines = [line.strip() for line in fstream if line.strip()]
    return lines


text_lines = get_text_lines("sherlock_holmes_adventures.txt")
# print(text_lines[:20])


# 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file

# SOLUTION:

def save_lines(destpath, lines, encoding="utf-8"):
    with open(destpath, mode="w", encoding=encoding) as file_out:
        for line in lines:
            line += "\n"
            file_out.write(line)


# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b

# SOLUTION:

save_lines("pure_sherlock.txt", text_lines)


# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")

# SOLUTION:

import string

def clean_punkts(srcpath, destpath, encoding="utf-8"):
    with open(srcpath, encoding=encoding) as fin, open(destpath, mode="w", encoding=encoding) as file_out:
        for line in fin:
            for char in line:
                if char in string.punctuation:
                    line = line.replace(char, "")
            file_out.write(line)


clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")


# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary


from collections import Counter
import csv

def get_word_usage(srcpath, destpath, encoding="utf-8"):
    with open(srcpath, encoding=encoding) as fin, open(destpath, mode="w", encoding=encoding) as file_out:
        words_list = csv.writer(file_out, delimiter=" ", quotechar="\n", quoting=csv.QUOTE_MINIMAL)
        words = []
        for line in fin:
            words += line.split()
        popular = Counter(words)
        words_list.writerow(popular.most_common())
        

get_word_usage("clean_sherlock.txt", "word_usage_sherlock.csv")