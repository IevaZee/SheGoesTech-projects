import os
from re import L
import string
from datetime import datetime as dt
from pathlib import Path

os.chdir("C:\\Users\\ievaz\\OneDrive\\Documents\\SheGoesTech-projects\\Day12")

# print(os.getcwd())

#  print(os.listdir())
# files = Path(".").glob("*")
# text_files = [f for f in Path(".").glob("*.txt") if f.is_file()]
# print(text_files)


with open("sherlock_holmes_adventures.txt", encoding="utf-8") as fstream:
    lines = fstream.readlines()
# print(text[:500])

print(len(lines))


with open("sherlock_holmes_adventures.txt", encoding="utf-8") as fin, open("destpath.txt", mode="w", encoding="utf-8") as file_out:
        for line in fin:
            if line.startswith("And"):
                file_out.write(line)