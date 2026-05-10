"""
This module demonstrates how to perform arithmetic operations using loops in Python.
It includes examples of using for loops to iterate over a list of numbers and perform various arithmetic operations
such as addition, subtraction, multiplication, and division.
"""

scores = [85, 90, 78, 92, 88, 95, 80, 91, 89, 94]

# Calculate total
total = 0
for score in scores:
    total += score
print(f"Total score: {total}")

# Calculate average
average = total / len(scores)
print(f"Average score: {average}")  

# Calculate maximum score
max_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score
print(f"Maximum score: {max_score}")

# Calculate minimum score
min_score = scores[0]       
for score in scores:
    if score < min_score:
        min_score = score
print(f"Minimum score: {min_score}")

# Calculate sum of even and odd scores
sum_even = 0
sum_odd = 0
for score in scores:
    if score % 2 == 0:
        sum_even += score
    else:
        sum_odd += score
print(f"Sum of even scores: {sum_even}")
print(f"Sum of odd scores: {sum_odd}")

# Calculate product of even and odd scores
product_even = 1
product_odd = 1
for score in scores:
    if score % 2 == 0:
        product_even *= score
    else:
        product_odd *= score
print(f"Product of even scores: {product_even}")
print(f"Product of odd scores: {product_odd}")

# Calculate sum of squares and sum of cubes
sum_squares = 0
sum_cubes = 0
for score in scores:
    sum_squares += score ** 2
    sum_cubes += score ** 3
print(f"Sum of squares: {sum_squares}")
print(f"Sum of cubes: {sum_cubes}")

# Calculate average of squares and average of cubes
average_squares = sum_squares / len(scores)
average_cubes = sum_cubes / len(scores)
print(f"Average of squares: {average_squares}")
print(f"Average of cubes: {average_cubes}")
