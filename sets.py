"""
This module contains the implementation of sets in Python. 
A set is an unordered collection of unique elements. 
Sets are mutable, meaning that you can add and remove elements 
from a set after it has been created. Sets are also iterable, 
which means that you can loop through the elements in a set.
"""

set1= {10,10,10,20,3,3.5, "Python", (1,2,3), True, False, None}
print(f"What is the datatype of set1 variable: {type(set1)}")
print(f"set1 value is: {set1}")
print(f"Length of set1 is: {len(set1)}")

# Membership operators for sets
nums = {1,3,2,0,-1}
print(f"Is 3 in nums set? {'Yes' if 3 in nums else 'No'}")
print(f"Is 5 in nums set? {'Yes' if 5 in nums else 'No'}")
# concatenation is not allowed.
# We can use the union operator to combine two sets. like sets mathimatical operations.
weekdays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
weekends = {"Saturday", "Sunday"}
days = weekdays | weekends
print(f"All days of the week: {days}")
dasys = weekdays.union(weekends)
print(f"All days of the week: {dasys}")
student1 = {"Physdics", "Chemistry", "Maths", "English"}
student2 = {"Biology", "Chemistry", "Maths", "History"}
student3 = {"Sanskrit", "Chemistry", "Maths", "Geography"}
common_subjects = student1 & student2 & student3
print(f"Common subjects among all students: {common_subjects}")
unique_subjects = student1 ^ student2 ^ student3
print(f"Unique subjects among all students: {unique_subjects}")
# subjects which are not common among all students but are common between any two students.
subjects = (student1 | student2 | student3) - common_subjects
print(f"Subjects which are not common among all students but are common between any two students: {subjects}")

# Frozen sets

frozen_set1 = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set 1: {frozen_set1}")
# frozen_set1.add(6) # This will raise an error because frozen sets are immutable.
# datatype of frozen set is frozenset
print(f"Datatype of frozen_set1: {type(frozen_set1)}")