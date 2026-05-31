"""
This module is dedicated for pickle python module.
Used to preserve python complex data structures and objects in a file and load them back when needed.
Pickle module is used to serialize and deserialize python objects.
Serialization is the process of converting a python object into a byte stream,
which can be saved to a file or transmitted over a network.
Deserialization is the process of converting a byte stream back into a python object.
Pickle module provides two main functions:
1. pickle.dump(obj, file): This function is used to serialize a python object and write
   it to a file. The obj parameter is the python object to be serialized,
   and the file parameter is the file object to which the serialized data will be written.
2. pickle.load(file): This function is used to deserialize a python object from a file.
   The file parameter is the file object from which the serialized data will be read.
"""

import pickle

# serialize a python object
# syntax: pickle.dump(object, file)
# object: the python object to be serialized
# file: the file object to which the serialized data will be written
with open(
    "D:\\learning_python\\learningpython\\file_samples\\student.pkl", "wb"
) as file:
    pickle.dump({"name": "John", "age": 20, "roll": 1}, file)

# deserialize a python object
# syntax: pickle.load(file)
# file: the file object from which the serialized data will be read
with open(
    "D:\\learning_python\\learningpython\\file_samples\\student.pkl", "rb"
) as file:
    student = pickle.load(file)
    print(student)

# example for multiple objects serialization and deserialization
students = [
    {"name": "John", "age": 20, "roll": 1},
    {"name": "Alice", "age": 21, "roll": 2},
    {"name": "Bob", "age": 22, "roll": 3},
]

with open(
    "D:\\learning_python\\learningpython\\file_samples\\students.pkl", "wb"
) as file:
    pickle.dump(students, file)

with open(
    "D:\\learning_python\\learningpython\\file_samples\\students.pkl", "rb"
) as file:
    students_data = pickle.load(file)
    print(students_data)

# example for handling errors while serializing and deserializing
try:
    with open(
        "D:\\learning_python\\learningpython\\file_samples\\student.pkl", "rb"
    ) as file:
        student = pickle.load(file)
        print(student)
except EOFError:
    print("End of file reached. Please check the file contents.")
except pickle.UnpicklingError:
    print("Error occurred while unpickling the object. Please check the file contents.")
except OSError:
    print("Something went wrong. Please check the file permissions.")

# when we have dictionary with multiple records and each record is a dictionary
# then we can use pickle module to serialize and deserialize the data.
# example of it.
students_dict = {
    "student1": {
        "roll": 1,
        "name": "John",
        "age": 20,
        "percentage": 85.5,
        "good_student": True,
    },
    "student2": {
        "roll": 2,
        "name": "Alice",
        "age": 21,
        "percentage": 90.0,
        "good_student": True,
    },
    "student3": {
        "roll": 3,
        "name": "Bob",
        "age": 22,
        "percentage": 92.5,
        "good_student": True,
    },
    "student4": {
        "roll": 4,
        "name": "Charlie",
        "age": 23,
        "percentage": 43.0,
        "good_student": False,
    },
    "student5": {
        "roll": 5,
        "name": "David",
        "age": 24,
        "percentage": 91.0,
        "good_student": True,
    },
}

with open(
    "D:\\learning_python\\learningpython\\file_samples\\students_dict.pkl", "wb"
) as file:
    pickle.dump(students_dict, file)

with open(
    "D:\\learning_python\\learningpython\\file_samples\\students_dict.pkl", "rb"
) as file:
    students_dict_data = pickle.load(file)
    print(students_dict_data)

# example for handling errors while serializing and deserializing
try:
    with open(
        "D:\\learning_python\\learningpython\\file_samples\\students_dict.pkl", "rb"
    ) as file:
        students_dict_data = pickle.load(file)
        print(students_dict_data)
except EOFError:
    print("End of file reached. Please check the file contents.")
except pickle.UnpicklingError:
    print("Error occurred while unpickling the object. Please check the file contents.")
except OSError:
    print("Something went wrong. Please check the file permissions.")

# if we need to read data line by line or record by record then we can use pickle.load()
# function in a loop until we reach the end of the file.
# example of it.
i = 0
with open(
    "D:\\learning_python\\learningpython\\file_samples\\students_dict.pkl", "rb"
) as file:
    while True:
        try:
            student = pickle.load(file)
            i += 1
            print(
                f"line number {i}: {student}"
            )  # print the line number and the student
        except EOFError:
            break
        except pickle.UnpicklingError:
            print(
                "Error occurred while unpickling the object. Please check the file contents."
            )
            break
        except OSError:
            print("Something went wrong. Please check the file permissions.")
            break

# if we want to store the dictionary records line by line and then need to read it line by line
# then we can use pickle.dump() function in a loop to write the records line by line
# and then use pickle.load() function in a loop to read the records line by line.
# example of it.
with open(
    "D:\\learning_python\\learningpython\\file_samples\\students_dict_line_by_line.pkl",
    "wb",
) as file:
    for student in students_dict.values():
        pickle.dump(student, file)

i = 0
with open(
    "D:\\learning_python\\learningpython\\file_samples\\students_dict_line_by_line.pkl",
    "rb",
) as file:
    while True:
        try:
            student = pickle.load(file)
            i += 1
            print(
                f"line number {i}: {student}"
            )  # print the line number and the student record
        except EOFError:
            break
        except pickle.UnpicklingError:
            print(
                "Error occurred while unpickling the object. Please check the file contents."
            )
            break
        except OSError:
            print("Something went wrong. Please check the file permissions.")
            break
