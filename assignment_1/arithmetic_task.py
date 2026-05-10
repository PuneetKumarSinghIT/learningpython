"""
This code will take two numbers as input from user and will perform addition, subtraction, multiplication and division on those numbers and will print the results.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
if num2 != 0:
    division = num1 / num2
    print("Division:", round(division,2))
else:
    division = "Undefined (division by zero)"
    print(division)