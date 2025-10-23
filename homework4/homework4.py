# Lists

# List Operations
favorite_food = ["pho", "thai curry", "sweet pork", "sushi", "steak"]

print(favorite_food[2]) # second food

print(favorite_food[-1:]) # last food

favorite_food.append("burrito") # adds burrito to the end of favorite food list
print(favorite_food)

favorite_food.insert(0, "apple") # adds apple to the front of the list
print(favorite_food)

del favorite_food[3] # deletes the third element in the list
print(favorite_food)

print(len(favorite_food)) # prints the length of the list

for food in favorite_food: # prints food in list as uppercase
    print(food.upper())

two_food = [favorite_food[0], favorite_food[-1]] # prints new list only show first and last food
print(two_food)

if "potato" in favorite_food:
    print("A potato!")
else:
    print("No potato!")

# Error encounter:
# line 29
#    else
#    ^^^^
# SyntaxError: invalid syntax
# Original code:
# if potato in favorite_food:
    #print("A potato!")
    #else
    #print("No potato!")
# Correction:
# Added "" to potato and added : to else

# Slicing and Striding 
numbers = list(range(21))
print(numbers)

def get_first_15(numbers):
    return numbers[:16]
print(get_first_15(numbers)) # returns 1 - 15 from the numbers list

first_15 = get_first_15(numbers)
def get_every_5th(lst):
    return lst[::5]
print(get_every_5th(first_15)) # returns every 5th number from the object first_15

every_5th = get_every_5th(first_15)
def reverse_and_stride(lst):
    reversed_lst = lst[::-1]
    return reversed_lst[::3]
print(reverse_and_stride(every_5th)) # returns every 3rd element from the object every_5th after reversing the list in the object

# Error encounter:
#    def reverse_and_stride(lst)
#                               ^
# SyntaxError: expected ':'
# Original code:
# every_5th = get_every_5th(first_15)
# def reverse_and_stride(lst)
#    reversed_lst - lst[::-1]
#    return reversed_lst[::3]
# print(reverse_and_stride(every_5th))
# Correction:
# I forgot : after def reverse_and_stride(lst), so I fixed it by adding : after.

# Nested Lists

# Nested List Operations
numbers_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers_2[2]) # returns the 3rd row of the nested list
# Error encountered:
# line 86, in <module>
#    print(numbers_2[3])
#          ~~~~~~~~~^^^
# IndexError: list index out of range
# Original code:
# print(numbers_2[3])
# Correction:
# I tried to grab an element in "position 3", but since 0 is the starting element, the list ends with 2, and 3 is out of range. I corrected this by replacing 3 with 2.

print(numbers_2[1][1]) # returns the 2nd item in the second row

numbers_2.append([10, 11, 12]) # creates a new row with elements 10, 11, and 12
print(numbers_2)

def sum_nested(n_lst):
    total = 0
    for row in n_lst:
        total += sum(row)
    return total
print(sum_nested(numbers_2)) # returns total value after adding all numbers from all rows

# Error encountered:
#  File "c:\Users\vangj\OneDrive\python_decal_fa25\Jacky\homework4\homework4.py", line 106, in <module>
#    print(sum_nested(numbers_2))
#          ^^^^^^^^^^^^^^^^^^^^^
#  File "c:\Users\vangj\OneDrive\python_decal_fa25\Jacky\homework4\homework4.py", line 104, in sum_nested
#    total += sum(row)
#    ^^^^^
# UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
# Original code:
# def sum_nested(n_lst):
#    for row in n_lst:
#        total += sum(row)
#    return total
# print(sum_nested(numbers_2))
# Correction:
# The total did not have an initial value attached to it, so I fixed it by setting total = 0.

# Create a 5x5 List
fivebyfive = []
num = 1
for i in range(5):
    row = []
    for j in range(5):
        row.append(num)
        num += 1
    fivebyfive.append(row)

def replace_3s(lst):
    new_lst = []
    for row in lst:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        new_lst.append(new_row)
    return new_lst

missing3_list = replace_3s(fivebyfive)
print(missing3_list)

def sum_no_q(lst):
    total = 0
    for row in lst:
        for item in row:
            if item != "?":
                total += item
    return total

sum_skip_q = sum_no_q(missing3_list)
print(sum_skip_q)

# Dictionaries

# Dictionary Operations
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"]) # prints Katie's age, 30

ages["Mira"] = 100 # replaces Mira's previous age, 48, with new age, 100

ages["Milana"] = 52 # adds Milana as a new element and sets her age to 52

del ages["Mariam"] # removes the element Mariam from the dictionary

for name, age in ages.items(): # returns each person's name and age
    print(name, age)

print(ages) # using print to check work done on this dictionary problem

# Favorite Function
fivebyfive = []
num = 1
for i in range(5):
    row = []
    for j in range(5):
        row.append(num)
        num += 1
    fivebyfive.append(row)

def replace_3s(lst):
    new_lst = []
    for row in lst:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        new_lst.append(new_row)
    return new_lst

missing3_list = replace_3s(fivebyfive)
print(missing3_list)