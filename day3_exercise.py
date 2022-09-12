# 1. Health check

# Ask user for their temperature.

# If the user enters below 35, then output "not too cold"

# If 35 to 37 (inclusive), output "all right"

# If the temperature  over 37, then output  "possible fever

# remember about type conversion if needed

t = float(input("What is your temperature? "))
if t < 35:
    print("not too cold")
elif 35 <= t <= 37:
    print("all right")
else:
    print("possible fever")