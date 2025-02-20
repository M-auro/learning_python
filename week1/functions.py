# Functions are block of reusable code that perform a specific task. You can define a function using the **def** keyword followed by the function name and parentheses. 
# The code block within every function starts with a colon **(:)** and is indented. 
# You can pass data, known as parameters, into a function. A function can return data as a result. To call a function, use the function name followed by parentheses.

# Example of a function without parameters
def greet():
    print("Hello, World!")

# Example of a function with parameters
def greetings(name):
    return f"Hello, {name}!"

# Calling the functions
greet()
print(greetings("Frodo"))