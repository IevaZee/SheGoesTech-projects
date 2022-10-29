# 2. Almost Hangman

# Write a program to recognize a text symbol

# The user (first player) enters the text.

# Only asterisks instead of letters are output.

# Assume that there are no numbers, but there may be spaces.

# The user (i.e. the other player) enters the symbol.

# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.

# Example:

# First input: Kartupeļu lauks -> ********* *****

# Second input: a -> *a****** *a***




# In principle, this is a good start to the game of hangman.

# https://en.wikipedia.org/wiki/Hangman_(game)


word = input("Enter a word: ")
asterisk = "*"
space = " "
new_text = ""

for c in word:
    if c == space:
        new_text += space
    else:
        new_text += asterisk

print(new_text)

while asterisk in new_text:
    letter = input("Guess a letter: ")
    for i, c in enumerate(word):
        if c == letter:
            new_text = new_text[:i] + letter + new_text[i+1:]
    print(new_text)

print(f"Congratulations! The word is '{word}'")