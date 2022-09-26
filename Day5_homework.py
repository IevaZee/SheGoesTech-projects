# write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string



text_1 = input("Please enter a text: ").lower()
text_2 = input("Please enter another text: ").lower()
output_text = ""

for i, c in enumerate(text_1):
    if c not in text_2: #FIXME compares only the first letter. Need a loop?
        print("Not all characters are in the second string")
        break
    else:
        for i, c1 in enumerate(sorted(text_2)):
            if c1 not in output_text:
                count = text_2.count(c1)
                output_text += f"{c1} {count}, " #FIXME don't need comma after the last letter
print(output_text) #FIXME gives extra empty output