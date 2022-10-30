import string

food = "kartupelis"
adjective = "dārgs "
# print(adjective + food)
# print(f"{adjective} ---- {food}")

drink = "beer"
# print(drink * 5)

# print("art" in food)
# print("music" in food)
# print(drink in food)

# print(len(food))

# print(food[0])
# print(food[1])
# print(food[9])
# print(food[-1])

# print(food[0:5], food[:5])
# print(food[-5:], food[-5:100])
# print(food[:])

# print(food[5:10], food[5:], food[-5:], sep="\n***\n")

start = 2
end = 6
text_len = 10
# print(food[start:end])

alphabet = string.ascii_lowercase
# print(alphabet)
new_alpha = alphabet[start:start+text_len]
# print(new_alpha, len(new_alpha))

# print(alphabet[::2])

# print(alphabet[::-1])
# reversed_alphabet = alphabet[::-1]
# print(reversed_alphabet)

# print("a" in alphabet)
# print(alphabet.index("a"))
# print(alphabet.index("s"))
# print(alphabet.index("bcd"))

# print(alphabet.find("s"))
# print(alphabet.find("S"))

# my_text = "Alice said 'Hello' and left."
# print(my_text)

# multi_line_string = f"""So now I can write whatever, even ' or " and so on"""
# print(multi_line_string)

# escaped_string = "text meaning \" and also \' and so on"
# print(escaped_string)

food = "auzu putra ar avenēm un krējumu"
# print(food)
# print(f"Min ({min(food)}), max ({max(food)}), len: {len(food)}")

# new_food = food.replace("u", "ū")
# print(new_food)
# new_food_2 = food.replace("u", "ū", count := 2)
# print(new_food_2)

# print("*"*len(food))

# ze_food = food[:3] + "OXOXO" + food[4:]
# print(ze_food)

# ze_food_2 = f"{food[:3]}OXOXO{food[4:]}"
# print(ze_food_2)

# cap_food = food.capitalize()
# print(cap_food)

# print(food.title())
# print(food.upper())
# print(food.lower())
# print("726264".isdecimal())
# print(food.isdecimal())

# dinner = "Putra ar krējumu"
# print(dinner.swapcase())

# print(food.count("a"))

# print(food.upper().replace("A", "Y"))


# for c in food:
#     print(c, end=":")


# count = 0
# bad_char = "a"
# clean_text = ""
# for c in food:
#     if c == bad_char:
#         count += 1
#         print("found a bad one", bad_char)
#     else:
#         clean_text += c
# print(f"There are {count} {bad_char} in {food}")
# print(f"Cleaned {clean_text=}")

# # OR

# # print(food.replace("a", ""))


# fresh_text = ""
# for c1, c2 in zip(food, clean_text):
#     if c1 == c2:
#         fresh_text += c1
#     else:
#         fresh_text += "_"
# print(fresh_text)


city = "      Rīga      "
print(city.strip())
print(city.rstrip())
print(city.lstrip())