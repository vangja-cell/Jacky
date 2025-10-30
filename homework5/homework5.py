# Homework 1 + 2 Review

# Vocabulary Review
# Git vs. GitHub
# Git is a control system that is installed locally on users' computers, and is used to manage code versions.
# GitHub is a web-based platform that hosts Git repositories in the cloud. It provides a centralized space for users to share Git code repositories and collaborate.

# Terminal vs. Command Line
# Terminal is the program or device that provides the text input and output environment. It allows users to type out commands and view results.
# Command Line is the interface, or area/line where users type out commands. 

# Local vs. Remote Repository
# Local repository is stored on a user's computer and contains all project files and full history of changes.
# Remote repository is hosted on a server via services like GitHub and is a central place for users to share and synchronize code changes.

# Version Control
# The practice of tracking, managing, and organizing changes made to files, typically source code.

# Staging Area
# A space where users prepare and organize changes that they want to include in their next commit. 

# git add
# Command used in Git to add changes from working directory to the staging area.

# git commit
# Command used to save changes that users prepared in the staging area to the local repository.

# git push
# Command used to upload commits from local Git repository to remote repository like GitHub.

# git status
# Command that provides real-time summary of the current state of Git repository, comparing working directory and staging area against the last committed snapshot.

# git pull
# Command used to update local Git repository with changes from a remote repository. 

# pwd
# Command that displays the full absolute path of the current directory.

# ls
# Command that list content inside of current directory.

# cd
# Command that allows users to move to a new directory, typically followed by absolute or relative path of desired directory.

# nano
# Command that allows users to make edits inside of a file.

# touch
# Command that allows users to create a file inside of their current directory.

# mv
# Command that allows users to move a file from one directory to another one.

# rm
# Command that deletes files and directories permanently from filesystem.

# cat
# Command used for displaying, concatenating, and creating text files.

# A Directory Tree

# Solutions to Questions
# pwd
# ls
# cd ~/python_decal/brianna_repo => git pull 
# mv homework.py ~/python_decal/judy_decal/homework
# *Assuming we are in the repository brianna_repo* => cd ../judy_decal/homework
# nano homework.py
# git add . => git commit -m "done with homework" => git push origin main
# git pull => git push | This error meant that Judy's local branch is out of sync with the remote branch.
# *Assuming we are in the repository homework* => cd ../../../Recent

# Homework 3 Review

# Data Types
def checkDataType(x):
    return type(x).__name__

print(checkDataType(3.14))
print(checkDataType(True))

# Conditionals
def evenOrOdd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(evenOrOdd(7))
print(evenOrOdd(10))

# Loops
def sumWithLoop(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# Homework 4 Review

# Lists
def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.extend([item, item])
    return new_list

print(duplicateList(['a', 'b', 'c']))

# Debugging
# Original Code
# def square(num)
#    return num * num
# Error: This original function forgot to put a ":" after the first line of code
# Correct Functional Code
def square(num):
    return num * num

print(square(4))

# Favorite Code
def checkDataType(x):
    return type(x).__name__

# Random Example
print(checkDataType("fruits"))