"""
Buildin- functions and user defined functions.
"""

# Build-in functions.
val = "Hellow world"
print(val)

# print is an in build function and even len is an in build function. we have list of in build functions in 
# python. we can use them without importing any module.
print(len(val))

# User defined functions.
def greet(name):
    return f"Hello {name}"

print(greet("Alice"))

# in user defined functions we can have any number of parameters and we can return any value. 
# we can also have default values for parameters.
def greetwell(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Alice"))
print(greetwell("Bob", "Hi"))

val_1 = int (input("Enter a number: "))
val_2 = int (input("Enter another number: "))
def opertions(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div

# We need to return the same number of values as we are trying to unpack. 
# In this case we are trying to unpack 5 values but we are only returning 4 values.
# So we need to return None for the fifth value.
# *exponent is used to unpack the remaining values in the return statement as list.
add, sub, mul, div, *exponent = opertions(val_1, val_2)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print(f"Exponent: {exponent}")

# types of funcitons arguments.
def func(a, b, c=3, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    
func(1, 2)
func(1, 2, 4)
func(1, 2, 4, 5)
func(1, 2, 4, 5, 6)
func(1, 2, 4, 5, 6, d=7, e=8)

# *args is used to pass a variable number of arguments to a function.
# **kwargs is used to pass a variable number of keyword arguments to a function.
# Default arguments always comes in last with respect to non default arguments.
# *args and **kwargs always comes in last with respect to default arguments.

# *args and **kwargs are used to pass a variable number of arguments to a function.
# *args is used to pass a variable number of arguments to a function.
# **kwargs is used to pass a variable number of keyword arguments to a function.
# Default arguments always comes in last with respect to non default arguments.
# *args and **kwargs always comes in last with respect to default arguments.

# Docstrings in functions.
def addition(a, b):
    """This function adds two numbers and returns the result.
    return the sum of a and b."""
    return a + b 
print(addition(2, 3))
print(addition.__doc__)
print(help(addition))
help(addition)

# Recursion in functions.
# Recursion is a process in which a function calls itself directly or indirectly.
# The main idea behind recursion is to break a problem into smaller subproblems and solve them recursively.
def factorial(n):
    """This function returns the factorial of a number n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Variables scope as local and global variables.
x = 10 # global variable
print(f"Global variable x: {x}")
def func():
    global x # global variable
    x = 100
    y = 20 # local variable
    print(f"Inside the function: x = {x}, y = {y}")
    print(f"Inside the function: x = {x}, y = {y}") 
func()
print(f"Outside the function: x = {x}")

# function as a parameter of another function.
def square(x):
    return x * x
def cube(x):
    return x * x * x
def my_func(call_another_function):
    return call_another_function(5)
print(f"Square of 5 is: {my_func(square)}")
print(f"Cube of 5 is: {my_func(cube)}")

# Lambda functions
# Lambda functions are anonymous functions that are defined using the lambda keyword.
# They are used to create small, one-time, and inline functions.
# They are also used to create higher-order functions.
# They are also used to create functions that take other functions as arguments.
# They are also used to create functions that return other functions.
# They are also used to create functions that take other functions as arguments.
# Lambda syntax: lambda arguments: expression
square = lambda x: x * x
cube = lambda x: x * x * x  
print(f"lambda function square of 5 is: {square(5)}")
print(f"lambda function cube of 5 is: {cube(5)}")
addition_sample = lambda a,b: a + b
print(f"lambda function addition of 2 and 3 is: {addition_sample(2, 3)}")

# filter and map functions with lambda functions.
# fileter and map functions syntax: filter(function, iterable) and map(function, iterable)
# filter function is used to filter the elements of a list based on a condition.
# map function is used to apply a function to each element of a list.
# filter and map functions are higher-order functions that take other functions as arguments.
# filter and map functions are used to create new lists based on the original list.
# filter function will select the element of list and filter it out.
# map function will return the value or modification done with the list elements.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter function is used to filter the elements of a list based on a condition.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers: {odd_numbers}")    
# map function is used to apply a function to each element of a list.
squared_numbers = list(map(lambda x: x * x, numbers))
print(f"Squared numbers: {squared_numbers}")        
cubed_numbers = list(map(lambda x: x * x * x, numbers))
print(f"Cubed numbers: {cubed_numbers}")