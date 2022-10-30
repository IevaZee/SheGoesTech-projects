# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile


for n in range(1,101):
    end = ", "
    if n == 100:
        end = ""
    if n%5 == 0 and n%7 == 0:
        print("FizzBuzz", end = end)
    elif n%5 == 0:
        print("Fizz", end = end)
    elif n%7 == 0:
        print("Buzz", end = end)
    else:
        print(f"{n}", end = end)