"""
This is a module for arithmetic operations in Python.
This module provides functions for addition, subtraction, multiplication and division of two numbers.
This module also provides functions for finding the square and cube of a number.
It is created by me as a user-defined module and can be imported in other python files.
"""

def func(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

def square(x):
    """This function returns the square of a number x."""
    return x * x

def cube(x):
    """This function returns the cube of a number x."""
    return x * x * x


if __name__ == "__main__":
    print(func(2, 3))
    print(square(4))
    print(cube(2))
    
# importance of __name__ == "__main__" in python.
# The __name__ variable is a built-in variable in python that is used to determine whether
# a python file is being run as the main program or being imported as a module in another python file.
# When a python file is run as the main program, the __name__ variable is set to "__main__".
# When a python file is imported as a module in another python file, the __name__
# variable is set to the name of the module.
