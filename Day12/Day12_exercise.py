# Exercise
# read text from  sherlock_holmes_adventures.txt

import os


# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len("sherlock_holmes_adventures.txt") -> 12305

# SOLUTION:

# def file_line_len(fpath):
#     with open(fpath, encoding="utf-8") as fstream:
#         lines = fstream.readlines()
#     return len(lines)

# ANOTHER SOLUTION - better for bigger files:

# def file_line_len(fpath):
#     file_len = 0
#     with open(fpath, encoding="utf-8") as fstream:
#         for _ in fstream:
#             file_len += 1
#     return file_len


# print(file_line_len("Day12\sherlock_holmes_adventures.txt"))


# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

# So we want to avoid/filter out those lines that contain whitespace

# PS preferably use encoding = "utf-8" when reading 

# SOLUTION:

# def get_text_lines(fpath):
#     with open(fpath, encoding="utf-8") as fstream:
#         lines = [line.strip() for line in fstream if line.strip()]
#     return lines


# text_lines = get_text_lines("Day12\sherlock_holmes_adventures.txt")
# print(text_lines[:20])


# 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file

# FIXME

with open("Day12\sherlock_holmes_adventures.txt", encoding="utf-8") as fin, open("destpath.txt", mode="w", encoding="utf-8") as file_out:
    for line in fin:
        if line.startswith("And"):
            file_out.write(line)





# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b

# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")


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