"""
This module demonstrates basic function usage in Python.
It includes examples of defining and calling functions with and without parameters.
"""

# Functions are block of reusable code that perform a specific task. You can define a function using
# the **def** keyword followed by the function name and parentheses. The code block within every
# function starts with a colon **(:)** and is indented. You can pass data, known as parameters, into
# a function. A function can return data as a result. To call a function, use the function name
# followed by parentheses.

# Example of a function without parameters
def greet():
    """Prints a greeting message."""
    print("Hello, World!")

# Example of a function with parameters
def greetings(name):
    """Returns a greeting message with the given name."""
    return f"Hello, {name}!"

# Calling the functions
greet()
print(greetings("Frodo"))
