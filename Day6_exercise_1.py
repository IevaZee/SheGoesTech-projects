# 1a. Average value

# Write a program that prompts the user to enter numbers (float).


# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered

# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.



### 1A solution:

# my_list = []

# while True:
#     numbers = input("Please enter a number or 'q' to quit: ")
#     if numbers == "q":
#         break
#     my_list.append(float(numbers))
#     avg_value = round((sum(my_list)/len(my_list)), 2)
#     print(f"The average value of the numbers is: {avg_value}")


### 1B solution:

# my_list = []

# while True:
#     numbers = input("Please enter a number or 'q' to quit: ")
#     if numbers == "q":
#         break
#     my_list.append(float(numbers))
#     avg_value = round((sum(my_list)/len(my_list)), 2)
#     print(f"The average value of the numbers {my_list} is: {avg_value}")


### 1C solution:

my_list = []

while True:
    numbers = input("Please enter a number or 'q' to quit: ")
    if numbers == "q":
        break
    my_list.append(float(numbers))
    avg_value = round((sum(my_list)/len(my_list)), 2)
    max_3_num = sorted(my_list)[-3:]
    min_3_num = sorted(my_list)[:3]
    print(f"The highest values are {max_3_num}, the lowest values are {min_3_num}. The average value is: {avg_value}.")