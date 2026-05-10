"""
This module contain detial about the conditions in python and how to use it.
If condition and it's usages.
Even ternary operator in python is also explained in this module.
"""

age = float(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
print("Congrats you have implemented the if condition statement.")


# if-else condition statement example:
# syntax is:
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false
age = float(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("Congrats you have implemented the if-else condition statement.")

# if-elif-else condition statement example:
# syntax is:
# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if both condition1 and condition2 are false
age = float(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative.")
elif age < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")
print("Congrats you have implemented the if-elif-else condition statement.")

# Is number is even or odd using if-else condition statement:
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
print(
    "Congrats you have implemented the if-else condition statement to check even or odd number."
)

# Nested if condition statement example:
# syntax is:
# if condition1:
#     if condition2:
#         # code to execute if both condition1 and condition2 are true
#     else:
#         # code to execute if condition1 is true and condition2 is false
number = int(input("Enter a number: "))
if number >= 0:
    if number % 2 == 0:
        print(f"{number} is a non-negative even number.")
    else:
        print(f"{number} is a non-negative odd number.")
else:
    print(f"{number} is a negative number.")
print("Congrats you have implemented the nested if condition statement.")

# Ternary operator in python:
# syntax is:
# variable = value_if_true if condition else value_if_false
age = float(input("Enter your age: "))
message = "You are eligible to vote." if age >= 18 else "You are not eligible to vote."
print(message)
print(
    "Congrats you have implemented the ternary operator in python to check if you are eligible to vote or not."
)
