"""
This module demonstrates basic file handling operations in Python.
It includes examples of reading from and writing to files.
"""

# File handling is used to read from and write to files.
# Python provides built in functions for creating, writing and reading files.

# Read from a file
# To read from a file, you can use the open() function.
# The open() function takes two arguments, the name of the file and the mode.
# The mode can be "r" for reading, "w" for writing and "a" for appending.
# You can also use "r+" for reading and writing.
# Example of reading from a file

with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


# Write to a file
# To write to a file, you can use the open() function with the mode "w".
# Example of writing to a file
with open("file.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!") # This will overwrite the content of the file
