# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.



text = input("Please enter a sentence: ")

reversed_text = [el[::-1] for el in text.lower().split()]

final_text = " ".join(reversed_text).capitalize()
print(final_text)