"""
If we create a python file and code it and give extension to it as .py then it is called a module. 
We can import the module in another python file and use the functions and variables defined in that module.
We can also import specific functions or variables from a module. 
We can also give an alias to the module while importing it. 
We can also import all the functions and variables from a module using * operator. 
We can also create our own modules and import them in other python files.
Modules are of two types: built-in modules and user-defined modules.
Built-in modules are the modules that are available in python by default. 
We can use them without importing them. 
User-defined modules are the modules that we create ourselves.
"""

# importing the built-in module math.
import math
print(f"Value of pi: {math.pi}")
print(f"Value of e: {math.e}")
print(f"Square root of 16: {math.sqrt(16)}")

# importing specific functions from math module.
from math import sqrt, pi
print(f"Square root of 16: {sqrt(16)}")
print(f"Value of pi: {pi}")

# importing all the functions and variables from math module.
from math import *
print(f"Square root of 16: {sqrt(16)}")
print(f"Value of pi: {pi}")

# importing module and giving it an alias.
# This module is a user-defined module that we have created in the same directory as this file.
import arithmetic as ar
print(f"Addition of 2 and 3: {ar.func(2, 3)}")
print(f"Square of 4: {ar.square(4)}")
print(f"Cube of 2: {ar.cube(2)}")
