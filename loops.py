# Loops are used to execute a block of code multiple times; Python accepts two types of loops for and while loops.

# A for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# The for loop does not require an indexing variable to set beforehand.

# Example of a for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)



# A while loop is used to execute a block of code multiple times as long as a condition is true.
# Example of a while loop
count = 0
while count < 5:
    print(count)
    count += 1


# The break statement is used to stop the loop before it has looped through all the items.
# Example of a break statement
count = 0
while count < 5:
    print(count)
    if count == 3:
        break
    count += 1


# The continue statement is used to stop the current iteration of the loop and continue with the next.
# Example of a continue statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

