# # 2. Cubes

# The user enters the beginning (integer) and end number.

# The output is the entered numbers and their cubes

# For example: inputs 2 and 5 (two inputs)

# Output

# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]




# PS could theoretically do without a list, but with a list it will be more convenient


start_numb = int(input("Please enter a start number: "))
end_numb = int(input("Please enter an end number: "))
all_cubes = []

numbers = list(range(start_numb, end_numb+1))

for number in numbers:
    cubed_numb = number**3
    all_cubes.append(cubed_numb)
    print(f"{number} cubed: {cubed_numb}")
print(f"All cubes: {all_cubes}")