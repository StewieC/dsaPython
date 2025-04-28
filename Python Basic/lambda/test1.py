"""
a lambda function is a small anonymous function that can take any number of arguments, 
but can only have one expression.
It is often used for short, throwaway functions that are not going to be reused elsewhere in the code.
"""

# lambda function to add 10 to a given number  
add10 = lambda x: x + 10
print(add10(5))  # Output: 15


# lambda functions can tke any number of arguments but can only have one expression
add = lambda x, y: x + y
print(add(5, 6))  # Output: 11

# multiplying two numbers
multiply = lambda x, y: x * y
print(multiply(5, 6))  # Output: 30