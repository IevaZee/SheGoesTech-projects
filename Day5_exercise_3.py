# 3. Text conversion

# Write a program for text conversion

# Save user input

# Print the entered text without changes

# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good



# Examples:

# The weather is not bad -> The weather is good

# The car is not new -> The car is not new

# This cottage cheese is not so bad -> This cottage cheese is good 

# Hints:

# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.

# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?



user_input = input("Enter a text: ")

bad_word_1 = "not"
bad_word_2 = "bad"
start_location = user_input.find(bad_word_1)
end_location = user_input.find(bad_word_2)
bad_word_2_len = len(bad_word_2) 
good_word = "good"

if start_location < end_location:
    print(f"{user_input[:start_location]}{good_word}{user_input[end_location+bad_word_2_len:]}")
else:
    print(user_input)