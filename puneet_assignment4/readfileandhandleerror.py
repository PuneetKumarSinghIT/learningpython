"""
This code is to :
Write a Python program that:
1. Opens and reads a text file named sample.txt
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exit.
"""

try:
    i = 0
    with open("D:\\learning_python\\learningpython\\puneet_assignment4\\sample.txt", "rt", encoding="utf-8") as file:
        for line in file:
            i += 1
            print(f"Line {i}: {line.strip()}")  # print the line number and the line content
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
