# WHILE LOOPS


# while True:
#     print("Do you want to continue?")


# i = 0
# while i < 5:
#     print("Hello No.", i)
#     print(f"Hello number {i}")
#     print(f"{i} squared is {i**2}")
#     i += 1
# print("The loop ends here")
# print("i is now", i)


# i = 10
# while i >= 0:
#     print("We are at the floor:", i)
#     if i == 0:
#         print("We have reached the garage")
#     i-= 2
# print("We are done with this. We are now at the floor", i)


# total = 0
# i = 20
# print(f"i is {i} total is {total}")
# while i <= 30:
#     total += i 
#     print(f"After adding {i} total is {total}")
#     i += 2
# print(f"i is {i} total is {total}")


# start = 50
# stop = 400
# step = 125
# i = start
# while i <= stop:
#     print(i)
#     print(f"i is {i}")
#     i += step
# print("After exiting loop i is", i)


# i = 10
# while True:
#     print("is is", i)
#     if i >= 14:
#         print("Ready to break out i is", i)
#         break
#     i += 2
# print("After break out i is", i)


# while True:
#     res = input("Enter a number or q to quit ")
#     if res == "q":
#         print("No more calculations today")
#         break
#     elif len(res) == 0:
#         print("You just pressed Enter. Please enter something!")
#         continue
#     elif res[0].isalpha():
#         print("I can't cube a letter")
#         continue
#     num = float(res)
#     cube = num**3
#     cube = round(cube, 2)
#     print(f"My calculator says that cube of {res} is {cube}")


# FOR LOOPS

# for num in range(5):
#     print("Number is", num)
# print("Out of loop", num)


# my_name = "Ieva Zee"
# for c in my_name:
#     print("Letter", c)
#     print(f"Letter {c} unicode is {ord(c)}")


# for my_num in range(100,111,2):
#     print(my_num)


# start = 10
# end = 37
# step = 4
# early_break = 28
# for my_num in range(start,end+1,step):
#     print(my_num)
#     if my_num > early_break:
#         print(f"Reached our early break threshold {early_break}")
#         break


# for _ in range(4):
#     print("We do not need a number this time")


# big_total = 0
# even_number_count = 0
# for i in range(1,5):
#     for j in range(1,3):
#         result = i * j
#         print(f"{i}*{j}={result}")
#         big_total += result
#         if result % 2 == 0:
#             print("Oh, even number", result)
#             even_number_count += 1
# print("Total is", big_total)
# print("Even number count is", even_number_count)


# for _ in range(10):
#     print("*", end="")


print(" "*10+"*"*6)