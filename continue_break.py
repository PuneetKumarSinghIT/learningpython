"""
This module will explain the use of continue and break statements in Python loops. 
The continue statement is used to skip the current iteration of a loop and move to the next iteration,
while the break statement is used to exit the loop entirely when a certain condition is met.
"""
# Example of using continue statement in a for loop
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(i)  # This will only print odd numbers
    
# Example of using break statement in a for loop
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is equal to 5
    print(i)  # This will print numbers from 1 to 4
    
