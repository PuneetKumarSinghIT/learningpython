"""
This module is created to learn json module in python.
"""
import json

students = {
    'student1':{'roll': 1, 'name': 'John', 'age': 20, 'percentage': 85.5, 'good_student': True},
    'student2':{'roll': 2, 'name': 'Alice', 'age': 21, 'percentage': 90.0, 'good_student': True},
    'student3':{'roll': 3, 'name': 'Bob', 'age': 22, 'percentage': 92.5, 'good_student': True},
    'student4':{'roll': 4, 'name': 'Charlie', 'age': 23, 'percentage': 43.0, 'good_student': False},
    'student5':{'roll': 5, 'name': 'David', 'age': 24, 'percentage': 91.0, 'good_student': True}
}

print(students)
print(type(students))

# dump the students dictionary to a json file
# syntax: json.dump(object, file, indent=4)
# object: the python object to be serialized to json format
# file: the file object to which the json data will be written
# indent: the number of spaces to be used for indentation
with open('D:\\learning_python\\learningpython\\file_samples\\students.json', 'wt', encoding='utf-8') as file:
    json.dump(students, file, indent=4)
    
# load the json data from the file and convert it back to a python dictionary
# syntax: json.load(file)
# file: the file object from which the json data will be read
with open('D:\\learning_python\\learningpython\\file_samples\\students.json', 'rt', encoding='utf-8') as file:
    students_data = json.load(file)
    print(students_data)
    
# json.load and json.loads are different and there difference is:
# json.load() is used to read JSON data from a file object
# json.loads() is used to parse a JSON string and convert it to a Python object
# json.dumps and json.dump are different and there difference is:
# json.dumps() is used to convert a Python object to a JSON string
# json.dump() is used to write JSON data to a file

# update the students dictionary and write it back to the json file
# syntax: json.dump(object, file, indent=4)

students_updated = {
    'student1':{'roll': 1, 'name': 'John', 'age': 20, 'percentage': 90.5, 'good_student': True},
    'student2':{'roll': 2, 'name': 'Alice', 'age': 21, 'percentage': 90.0, 'good_student': True},
    'student3':{'roll': 3, 'name': 'Bob', 'age': 22, 'percentage': 34.5, 'good_student': False},
    'student4':{'roll': 4, 'name': 'Charlie', 'age': 23, 'percentage': 89.0, 'good_student': True},
    'student5':{'roll': 5, 'name': 'David', 'age': 24, 'percentage': 91.0, 'good_student': True}
}

with open('D:\\learning_python\\learningpython\\file_samples\\students.json', 'rt', encoding='utf-8') as file:
    students_data_to_manupulate = json.load(file)
    print(students_data_to_manupulate)
    
students_data_to_manupulate.update(students_updated)

with open('D:\\learning_python\\learningpython\\file_samples\\students.json', 'wt', encoding='utf-8') as file:
    json.dump(students_data_to_manupulate, file, indent=4)

with open('D:\\learning_python\\learningpython\\file_samples\\students.json', 'rt', encoding='utf-8') as file:
    students_data_updated = json.load(file)
    print(students_data_updated)  
   