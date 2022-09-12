# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.

# Task. Ask the user for the amount of the monthly salary and the number of years worked.

# Calculate the bonus.

# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)

bonus_percent = 0.15
years_without_bonus = 2
salary = float(input("What is your monthly salary? "))
years_worked = float(input("How many years have you worked? "))
# bonus = 0.15 * salary * years
if years_worked > years_without_bonus:
    print(f"Your Christmas bonus will be {bonus}")
else:
    print("Sorry, no Christmas bonus for you yet")