"""
Wrtie a program for summing the integers from  to 50.
1. Uses a loop to iterate over numbers from 1 to 50.
2. Calculates the sum of all integers in this range.
3. Displays the final sum.
"""

total_sum = 0

for i in range(1,51):
    total_sum += i
 
print(f"The sum of integers from 1 to 50 is: {total_sum}")
