"""
This module will explain the use of the random module in Python.
We will import the random module and use its functions to generate random numbers, 
select random items from a list, and shuffle a list.
"""

import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print("Random integer between 1 and 10:", random_integer)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)

# randint(a, b) returns a random integer N such that a <= N <= b.
# random() returns a random float in the range [0.0, 1.0).
# randrange(a, b) returns a random integer N such that a <= N < b.
# randrange(a, b, c) returns a random integer N such that a <= N < b, and N is a multiple of c.

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.random())  # Random float between 0 and 1
print(random.randrange(1, 10))  # Random integer between 1 and 9
print(random.randrange(1, 10, 2))  # Random odd integer between 1 and 9

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)

# Select a random item from a list
my_list = ["apple", "banana", "cherry", "date"]
random_item = random.choice(my_list)
print("Random item from the list:", random_item)