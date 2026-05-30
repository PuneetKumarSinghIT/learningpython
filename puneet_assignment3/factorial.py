"""
This program is for factorial of a number using recursion in python.
and iteration in python.
"""

num = int(input("Enter a number to find its factorial: "))

# finding factorial by using iteration.
def factorial_iterative(n):
    """This function finds the factorial of a number n using iteration."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Factorial of {num} using iteration is: {factorial_iterative(num)}")

# finding factorial by using recursion.
def factorial_recursive(n):
    """This function finds the factorial of a number n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
print(f"Factorial of {num} using recursion is: {factorial_recursive(num)}")