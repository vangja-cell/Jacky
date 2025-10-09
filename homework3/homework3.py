# Print Functions

# Say Goodbye
def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("Jacky") # => Goodbye, Jacky

# Area of a Circle
def circle_area(pi, r):
    print(pi * (r ** 2))
circle_area(3.14, 4) # => 50.24

# Return Functions

# Subtract, Multiply and Divide 
# Subtract
def subtract(a, b):
    return a - b
s = subtract(23, 17)
print(s) # => 6

# Multiply
def multiply(a, b):
    return a * b
m = multiply(9, 4)
print(m) # => 36

# Divide
def divide(a, b):
    return a / b
d = divide(88, 8)
print(d) # => 11.0

# Conditionals

# What Should I Wear?
def maxmin_temp(readings):
    return (min(readings), max(readings))
readings = [15, 14, 17, 20, 23, 28, 20]
result = maxmin_temp(readings)
print(result) # => (14, 28)

# Check if it's the Weekend
def is_weekend(day):
    if day == 6 or day == 7:
        return "True"
    else:
        return "False"
print(is_weekend(6)) # => True

# Fuel Efficieny Calculator 
def mpg(miles, gallons):
    return miles / gallons
print(mpg(400, 25)) # => 16.0

# Secret Code
def secret_code(n):
    last_digit = n % 10
    rest = n // 10
    digits = len(str(rest))
    return last_digit * (10 ** digits) + rest
print(secret_code(34587)) # => 73458

# Loops

# Oski Stole Your Power
def expo(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result
print(expo(3, 4)) # => 81

# Min & Max with Loops!

# For Loops
# Minimum value
def find_min(num_list):
    current_min = num_list[0]
    for number in num_list[1:]:
        if number < current_min:
            current_min = number
    return current_min
num_list = [1, 5, 2, 7, 3, 6, 8, 9]
print(find_min(num_list)) # => 1
# Maximum value
def find_max(num_list):
    current_max = num_list[0]
    for number in num_list[1:]:
        if number > current_max:
            current_max = number
    return current_max
num_list = [1, 5, 2, 7, 3, 6, 8, 9]
print(find_max(num_list)) # => 9

# While Loops
# Minimum value
def find_minv(num_list):
    i = 0
    min_value = None
    while i < len(num_list):
        if min_value is None or num_list[i] < min_value:
            min_value = num_list[i]
        i += 1
    return min_value
num_list = [1, 5, 2, 7, 3, 6, 8, 9]
print(find_minv(num_list)) # => 1
# Maximum value
def find_maxv(num_list):
    i = 0
    max_value = None
    while i < len(num_list):
        if max_value is None or num_list[i] > max_value:
            max_value = num_list[i]
        i += 1
    return max_value
num_list = [1, 5, 2, 7, 3, 6, 8, 9]
print(find_maxv(num_list)) # => 9

# Calculate the Sum
def sum_n(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
print(sum_n(2468)) # => 20

# Favorite Function
    # What Should I Wear?
def maxmin_temp(readings):
    return (min(readings), max(readings))
readings = [15, 14, 17, 20, 23, 28, 20]
result = maxmin_temp(readings)
print(result)

readings = [15, 14, 17, 20, 23, 28, 20]
result = maxmin_temp(readings) # outputs min = 14 and max = 28 as a tuple => (14, 28)

print(f"The result of What Should I Wear (5.1) with the readings being [15, 14, 17, 20, 23, 28, 20] is (14. 28).")
