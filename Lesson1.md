
# Python: Week 1

## Topics Covered
- Variables
- Loops
- Functions
- File Handling

### Variables

Variables are used to store data that can be used and manipulated throughout your program. In Python, you don't need to declare the type of a variable explicitly; it is inferred from the value you assign to it.

```python
# Example of variables
x = 10          # Integer
y = 3.14        # Float
name = "Frodo"  # String
is_active = True  # Boolean

```

`Run the scprit with python3 variables.py`

### Loops

Loops are used to execute a block of code repeatedly. Python supports `for` and `while` loops.

The loop variable does not need to be defined beforehand; it is defined within the context of the `for` loop.

### For Loop

A `for` loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).

```python
# Example of a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

`Run the scprit with python3 loops.py`

### While Loop

A `while` loop is used to execute a block of code as long as a condition is true.

```python
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

```

### Functions

Functions are blocks of reusable code that perform a specific task. You can define your own functions using the `def` keyword.

```python
# Example of a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Frodo"))

```

### File Handling

File handling is used to read from and write to files. Python provides built-in functions to handle files.

### Reading a File

```python
# Example of reading a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

```

### Writing to a File

```python
# Example of writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, world!")

```