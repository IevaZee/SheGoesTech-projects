import os
from re import L
import string
from datetime import datetime as dt
from pathlib import Path


print(os.getcwd())

#  print(os.listdir())
# files = Path(".").glob("*")
# text_files = [f for f in Path(".").glob("*.txt") if f.is_file()]
# print(text_files)


with open("Day12\sherlock_holmes_adventures.txt", encoding="utf-8") as fstream:
    lines = fstream.readlines()
# print(text[:500])

print(len(lines))