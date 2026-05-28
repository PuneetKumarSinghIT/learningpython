"""
This module is a simple example of a while loop in Python. 
It demonstrates how to use a while loop to repeat a block of code until a certain condition is met.
"""
number = 0  # Initialize the number variable
while number < 10:
    print("The number is:", number)
    number += 1  # Increment the number by 1 to avoid an infinite loop  

print("The loop has finished.")

print(
    "Congrats you have implemented the while loop in python to repeat a block of code until a certain condition is met."
)

# Infinite while loop example (commented out to prevent execution)
# while True:
#     print("This will run forever!")
# To stop an infinite loop, you can use a break statement or a condition that eventually becomes false.

# Example to make a infinite loop but stop in certain condition

while True:
    stop = input("Type 'stop' to end the loop: ")
    if stop.lower() == 'stop':
        print("Loop has been stopped.")
        break  # Exit the loop when the user types 'stop'
    else:
        print("Type 'stop' to kill the loop as you typed:", stop)
        
# Read collection values in a while loop
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print("Fruit at index", index, "is", fruits[index])
    index += 1  # Move to the next index
    
# while loop with else block
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print("Fruit at index", index, "is", fruits[index])
    index += 1  # Move to the next index
else:
    print("All fruits have been printed.")
