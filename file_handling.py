"""
This module is for file handling and to learn it like a pro.
"""
# file can be of any format. text file, binary file, csv file, json file, etc.
# open file method
# syuntax: open(file_name, mode)
# mode can be 'r' for read, 'w' for write, 'a' for append, 'x' for create, 'b' for binary, 't' for text
# by default mode is 'r' for read and 't' for text
# file_name is a complete path of the file on which we need to work.
# open file in read mode
file = open('D:\\learning_python\\learningpython\\file_samples\\practice.txt', 'rt')
print(file) # it is a file object which we have opened.

# closing a file
# syntax: file.close()
file.close() # it is important to close the file after working with it to free up system resources.

# creating a file
# syntax: open(file_name, mode)
# mode for creating a file is 'x' for create. it will create a file if it does not exist, 
# otherwise it will raise an error.
# If a file already exists with the same name, it will raise a FileExistsError. 
# So, we can use try-except block to handle this error.
# We need to give new name to create a new file if the file with the same name already exists.
try:
    file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'xt')
    print('File created successfully.')
except FileExistsError:
    print('File already exists. Please choose a different name.')
    
# writing a content in a file
# syntax: file.write(content)
# mode for writing a file is 'w' for write. it will create a file if
# it does not exist, otherwise it will overwrite the existing file.
# If a file is opened with 'w' then file get truncated to zero length, 
# so all the existing content will be deleted.
# as it will allow us to write new content to the file.
file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'wt')
file.write('This is a new file created for learning file handling in Python.\n')
file.write('We are learning File handling in Python.\n')
file.write('Modes to open a file are: r, x, w, a, t, b\n')
file.close()

# example of overwriting the exisitng file.
# If a file don't exit then w mode created a new file and write the content in it, 
# but if a file already exists with the same name then 
# it will overwrite the existing file with new content.
file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'wt')
file.write('File is overwritten with new content.\n')
file.write('This is a new file created for learning file handling in Python.\n')
file.write('We are learning File handling in Python.\n')
file.close()

# reading a file
# syntax: file.read(size) - It will help to run only the desired characters from the file. 
# It will read the content of the file and return it as a string.
# mode for reading a file is 'r' for read. it will read the content of the file.
# if we don't specify the size then it will read the entire content of the file.
# read() function will read the content of the file and return it as a string.
file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
content = file.read()
print(content)
print(type(content)) # it will return the type of the content which is string.
file.close()

# readline() function will read the content of the file and return it as a list of lines.
# it will read the first line of the file and return it as a string. 
# if we call readline() function again then it will read 
# the next line of the file and return it as a string.
file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
line = file.readline()
print(line)
print(type(line)) # it will return the type of the line which is string.
file.close()

# readlines() function will read the content of the file and return it as a list of lines.
# it will read all the lines of the file and return it as a list of strings.
file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
lines = file.readlines()
print(lines)
print(type(lines)) # it will return the type of the lines which is list.
file.close()

for line in lines:
    print(line.rstrip('\n')) # it will remove the newline character from the end of the line.
    
# appendign the file with new content.
# syntax: file.write(content)
# mode for appending a file is 'a' for append. it will create a file
# if it does not exist, otherwise it will append the new content to the existing file.
# If file does not exit then it will create a new file and write the content in it, 
# but if a file already exists with the same name then it will 
# append the new content to the existing file.
file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'at')
file.write('\nThis is an appended line.\n')
file.write('a mode is used to append the content of file and new content start from end of the file.\n')
file.close()

# with statemet for file handling
# syntax: with open(file_name, mode) as file:
# it will automatically close the file after working with it, so we don't need to call file.close() method.
# It will close the resources after working with the file, 
# so it is a good practice to use with statement for file handling. 
# Even though error occurs in the block of code, it will still close the file.
with open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt') as file:
    content = file.read()
    print(content)

print(f'content: {content}') # it will print the content of the file (content)

# check if file exists or not.
# by using the os.path.exists() function we can check if a file exists or not.
import os
file_path = 'D:\\learning_python\\learningpython\\file_samples\\new_file.txt'
if os.path.exists(file_path):
    print('File exists. By using os.path.exists() method.')
else:
    print('File does not exist.')
    
# by using pathlib module we can also check if a file exists or not.
# method name is Path.exists() which will return True if the file exists, otherwise it will return False.
from pathlib import Path
file_path = Path('D:\\learning_python\\learningpython\\file_samples\\new_file.txt')
if file_path.exists():
    print('File exists. Checked by using pathlib module. Method name is Path.exists().')
else:
    print('File does not exist.')
    
# common issues with file handling
# 1. FileNotFoundError: This error occurs when we try to open a file that does not exist.
# 2. PermissionError: This error occurs when we try to open a file that we don't have permission to access.
# 3. IOError: This error occurs when there is an input/output error while working with the file.
# 4. Opening a file for read but try to write in it, it will raise an error.
# 5. Opening a file for write but try to read from it, it will raise an error.
# 6. wt mode will truncate the file and as a result we will lose all the existing content of the file, 
# so we need to be careful while using wt mode. So avoid to use the w mode.
# 7. x mode will raise an error if the file already exists, 
# so we need to handle this error by using try-except block.
# Way to handle these errors is by using try-except block to catch the exceptions and handle them gracefully.
# Two classification of errors or exceptions are:
# 1. SyntaxError: This error occurs when there is a syntax error in the code. compile time error.
# 2. Exception: This error occurs when there is an error during the execution of the code. runtime error.

# example of handling FileNotFoundError
try:
    file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('File not found. Please check the file path.')

# example of handling PermissionError
try:
    file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('File not found. Please check the file path.')
except PermissionError:
    print('Permission denied. Please check the file permissions.')
    
# example of handling IOError
try:
    file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('File not found. Please check the file path.')
except PermissionError:
    print('Permission denied. Please check the file permissions.')
except IOError:
    print('Input/output error. Please check the file permissions.')
    
# example of handling IOError and unknown errors.
try:
    file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('File not found. Please check the file path.')
except PermissionError:
    print('Permission denied. Please check the file permissions.')
except IOError:
    print('Input/output error. Please check the file permissions.')
except:
    print('Something went wrong. Please check the file permissions.')
    
# Exceptions handling - else and finally block
# else block will execute if there is no exception in the try block.
# finally block will execute whether there is an exception or not.
# finally block is used to close the file after working with it, 
# so we don't need to call file.close() method in the try block.
# example of using else and finally block for file handling
try:
    file = open('D:\\learning_python\\learningpython\\file_samples\\new_file.txt', 'rt')
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print('File not found. Please check the file path.')
    print(e) # it will print the error message of the exception.
except PermissionError as e:
    print('Permission denied. Please check the file permissions.')
    print(e) # it will print the error message of the exception.
except IOError as e:
    print('Input/output error. Please check the file permissions.')
    print(e) # it will print the error message of the exception.
except:
    print('Something went wrong. Please check the file permissions.')
    print(e) # it will print the error message of the exception.
else:
    print('File read successfully. No exception occurred.')
finally:
    try:
        file.close()
        print('File closed successfully.')
    except:
        print('Error while closing the file.')
        
# raise an exception manually
# syntax: raise ExceptionType('Error message')
# example of raising an exception manually
def read_file(file_path):
    """Read and return the text content from the given file path."""
    if not os.path.exists(file_path):
        raise FileNotFoundError('File not found. Please check the file path.')
    else:
        with open(file_path, 'rt') as file:
            content = file.read()
            return content
try:    
    content = read_file('D:\\learning_python\\learningpython\\file_samples\\new_file45.txt')
    print(content)
except FileNotFoundError as e:
    print(e) # it will print the error message of the exception.        