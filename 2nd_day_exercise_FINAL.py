# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS:
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
import datetime
current_year = datetime.datetime.now(). year
username = input("What is your username? ")
print(f"{username}, you have a nice name!")
age_now = int(input(f"How old are you {username}? "))
target_age = 100
years_to_go = target_age - age_now
print(f"{username}, you will be 100 years old in {years_to_go} years 🙂")
year_in_which_user_will_be_100 = current_year + years_to_go
print(f"{username}, you will be {target_age} years old in year {year_in_which_user_will_be_100}")