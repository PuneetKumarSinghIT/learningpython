"""
First String Example in Python is slicing.
This is a simple slicing example in Python.
It will include the end index but exclude the start index.
"""

name = "Puneet Kumar Singh"
print("middle name is:", name[7:12:1])
print("reandom name is:", name[0:12:2])
print("reverse name is:", name[1:30:4])
print(len(name))

"""
Second example is for formatting string in Python.
This is a simple example of string formatting in Python.
"""

name = "Puneet"
age = 25

# without fstring
print("My name is " + name + " and I am " + str(age) + " years old.")

# with fstring
print(f"My name is {name} and I am {age} years old.")
