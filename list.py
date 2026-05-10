"""
This module is to analyze list in python and it's characteristics.
"""

name = "John"
age = 30
percentage = 85.5

students = ["John", 30, 85.5]

print(f"What is the datatype of students variable: {type(students)}")
print(f"students value is: {students}")


l1 = [1, 2, 3, 4, 5]
l2 = [0,5]

print(l1 + l2) # concatenation of two lists
print(l2 * 3) # repetition of list l2 three times
# print(l1 * l2) # repetition of list l1 two times it will give error as list cannot be used to direct another list for repetition.

# Append method is used to add an element at the end of the list.
l1.append(6)
print(l1)

# insert method is used to add an element at a specific index in the list.
l1.insert(2, 0) # it will insert 0 at index 2
print(l1)

# extend, remove, pop
l1.extend(l2) # it will add all the elements of l2 to l1
print(l1)
l1.remove(0) # it will remove the first occurrence of 0 from l1
print(l1)
l1.pop() # it will remove the last element from l1
print(l1)
l1.pop(2) # it will remove the element at index 2 from l1
print(l1)

#numerical oprations on list
numbers = [1, 2, 3, 4, 5]
# smallest number in the list
print(f"The smallest number in the list is: {min(numbers)}")
# largest number in the list
print(f"The largest number in the list is: {max(numbers)}")
#  sum of all the numbers in the list
print(f"The sum of all the numbers in the list is: {sum(numbers)}")
# length of the list
print(f"The length of the list is: {len(numbers)}")
