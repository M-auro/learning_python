"""
This module demonstrates basic loop usage in Python.
It includes examples of for loops, while loops, and the use of break and continue statements.
"""

# Loops are used to execute a block of code multiple times; Python accepts two types of loops:
# for and while loops.

# A for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# The for loop does not require an indexing variable to set beforehand.

# Example of a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# A while loop is used to execute a block of code multiple times as long as a condition is true.
# Example of a while loop
COUNT = 0
while COUNT < 5:
    print(COUNT)
    COUNT += 1

# The break statement is used to stop the loop before it has looped through all the items.
# Example of a break statement
COUNT = 0
while COUNT < 5:
    print(COUNT)
    if COUNT == 3:
        break
    COUNT += 1

# Continue statement is used to stop the current iteration of the loop and continue with the next.
# Example of a continue statement
COUNT = 0
while COUNT < 5:
    COUNT += 1
    if COUNT == 3:
        continue
    print(COUNT)
