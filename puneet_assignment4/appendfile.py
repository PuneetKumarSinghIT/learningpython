"""
Write a Python program that:
1. Takes user input and writes it to a file named output.txt
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.
"""

input = input("Enter some text to write to the file: ")

with open("D:\\learning_python\\learningpython\\puneet_assignment4\\output.txt", "wt", encoding="utf-8") as file:
    file.write(input + "\n")  # write the user input to the file and add a newline character

with open("D:\\learning_python\\learningpython\\puneet_assignment4\\output.txt", "a", encoding="utf-8") as file:
    file.write("This is additional data appended to the file.\n")  # append additional data to the file

with open("D:\\learning_python\\learningpython\\puneet_assignment4\\output.txt", "rt", encoding="utf-8") as file:
    print("Final content of the file:")
    print(file.read())  # print the content of the file line by line
