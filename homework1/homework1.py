File: homework1. py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5 
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, real part 3 and imaginary part j

d = "hello"
print(d)
print(type(d)) # d is a string, a data type that holds text

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a structure that stores a collection of elements in a specific order

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a built-in, unordered collection that stores data in key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is an integer, whole numbers with no decimals

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a structure that stores a collection of elements in a specific order

i = True
print(i)
print(type(i)) # i is a logical, a data type that holds only two possible values

j = None
print(j)
print(type(j)) # j is a NoneType, a special constant that represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a structure that stores a collection of elements in a specific order

l = str(14)
print(l)
print(type(l)) # l is a string, a da, ta type that represents a sequence of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a number with decimals

# --- Questions ---

# 1. There are 8 different data types
# 2. integer, float, complex number, string, list, dictionary, logical, nonetype
# 3. a & g = integer
#    b & m = float
#    d & l = string
#    e, h, & k = list
# 4. The data type of l is string and not integer because the function str() converts 14 into a string data type.
# 5. n = (1, 2, "decal") | print(n) | print(type(n)) # n is a tuple, an ordered, immutable sequence of elements

# --- Booleans ---

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 does not equal 9
print(10 <== 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, "abc" is a non-empty string
print(bool(123)) # True, 123 is a non-empty integer
print(bool(["apple", "cherry", "banana"])) # True, ["apple", "cherry", "banana"] is a non-empty list
print(bool(True)) # True, True = True
print(bool(False)) # False, False = False
print(bool(0)) # False, 0 = False
print(bool("")) # False, "" is empty
print(bool(" ")) # True, " " is non-empty
print(bool(())) # False, () is empty
print(bool([])) # False, [] is empty
print(bool({})) # False, {} is empty
print(bool(True and False)) # False, both logicals are not True
print(bool(True and True)) # True, both logicals are True
print(bool(False and False)) # False, both logicals are False
print(bool(True or False)) # True, or only requires one element to be True
print(bool(True or True)) # True, there are only True in or operator
print(bool(False or False)) # False, there are only False in or operator
print(bool(not(False))) # True, not inverts False to True
print(bool(not(True))) # False, not inverts True to False

# --- Questions ---

# 1. Outputs True if expression is logical or if function is not empty.
#    Outputs False if expression if illogical or if function is empty.
#    If expression cannot give output that is "fully" True then False is the output. 
#    Expression bool(not()) should be intuitive
# 2. The expression with the most surprising result is bool(True or False).
# 3. bool(1) because 1 = True in logical
# 4. bool(None) because None = absence of value = False in logical

# --- Operators ---

# --- Arithmetic Operators ---
print(10 + 5) # 15, + perform addition
print(10 - 5) # 5, - perform subtraction
print(2 * 4) # 8, * perform multiplication
print(6 / 3) # 2, / perform division
print(5 % 2) # 1, % returns remainder of a division operation
print(3 ** 2) # 9, ** perform exponentiation
print(15 // 2) # 7, // perform division and rounds down to the nearest whole number

# --- Comparison Operators ---
print(5 == 2) # False, 5 does not equal 2
print(10 != 10) # False, != evaluates if 10 is not equal 10, but here 10 = 10
print(2 < 5) # True, 2 is less than 5
print(12 > 5) # True, 12 is greater than 5
print(5 <= 6) # True, although not equal to 6, 5 is less than 6
print(1 >= 10) # False, 1 is not greater than or equal to 10

# --- Assignments Operators ---
x = 5
x += 5 # x = 10, += perform x = x + 5
x -= 4 # x = 1, -= perform x = x - 4
x *= 3 # x = 15, *= perform x = x * 3

# --- Logical Operators ---
# 1. The operator and is a logical operator that is used to combine two or more conditions.
#    bool(True and True) | bool(True and False)
# 2. The operator or is a logical operator that combines conditions. It stops evaluating when a True value is found.
#    bool(True or False) | bool(False or False)
# 3. The operator not performs logical negation and inverts the truth value of a Boolean expression
#    bool(not(False)) | bool(not(True))

# --- More Questions ---
# 1. The / is a division operator that outputs floats, or decimal numbers
#    The // is also a division operator, but it rounds the resulting value down to an integer
# 2. The // is a division operator that rounds the output down to an integer
#    The %  is a division operator that outputs the remainder of a division operation
# 3. I would use the % operator. 
#    print(10 % 4) => 2
# 4. Assignment operators reassigns the variable, in this case x, to a new value that is the previous value of x +/-/* an inserted numeric.

# --- Strings ---

my_string = "hello"

# --- Mutations ---
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello

# --- Questions ---
# 1. Slicing means to extract a portion of a sequence. 
#    We used slicing in mutations 8 and 9
# 2. These lines of codes results in the phrase "Hello, my name is Oski" where the content of the variable name is inserted into the quote.
# 3. These lines of codes results in the phrase "Hello, my name is Oski", but I am not sure what f does.
# 4. The difference between these last two print is that in the first print, ", name" inserts the content of the variable into the quote. However, the f, which is a f-string, in the second print will replace the variable name inside of the curly brackets with its content.

# --- Terminal Commands --- 

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# List the content inside of a folder or directory
# Example: ls Desktop

# ls -a
# List files and directories in specified location, including hidden ones
# Example: ls -a Desktop

# mkdir
# Make directory. Creates a new folder or directory at a specified path
# Example: mkdir q_test_file

# cat
# Concatenate. Prints out all the contents of a file
# Example: cat homework1.py

# pwd
# Print working directory. Shows the folder or directory you are currently in
# Example: pwd => /c/Users/"name"

# cd ..
# Move directory back up one, or go back one.
# Example: cd .. will perform ~/Desktop => ~

# cd .
# Move directory to current directory.
# Example: cd . will perform ~/Desktop => ~/Desktop

# cp
# Copies files and directories
# Example: cp homework1.py homework1.0.py

# mv
# Moves a file or directory to a new location or path
# Example: mv homework1.py ~/Desktop/testing_folder

# rm
# Removes files and directories permanently
# Example: rm hwtesting.py

# clear
# Clears the terminal screen, removing visible texts, commands, and outputs
# Example: clear performs ls ~/Desktop => *blank*

# grep
# Global regular expression print. Searches plain-text data for lines that match a regular expression
# Example: grep "Questions" homework1.py

# --- Questions ---
# 1. find: locate files and directories within specified directory hierachy based on criteria
#          find [path] [expression for criterias]
#    tar: combine files and directories into an archive file
#         tar -cvf => c creates archive, v shows files being added, f specifies archive name
#    touch: creating empty files and updating file timestamps
#           touch newfile to make new file or touch oldfile to update file's timestamps
# 2. ls and ls -a are different because ls will list files in a folder or directory while ls -a will do the same but also list hidden files and can be specified.
# 3. A hidden file is invisible by default in file browsers to avoid accidental disruption or deletion.
# 4. -l: provides a long listing format with detailed information
#        ls -l to see a file's owner and size
#    -r: applies a command to a directory and its content
#        rm -r to remove a directory and its content
#    -p: creates parent directories as needed
#        mkdir -p to show path of new directory
