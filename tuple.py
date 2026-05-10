"""
This module is create to understand tuple data structure and it's usage.
"""

t1 = (1, 3, 2, "Python", 3.12, True, [1, 2, 3], (4, 5, 6), {"name": "Puneet"})
print(f"What is the datatype of t1 variable: {type(t1)}")
print(f"t1 value is: {t1}")

t1 = (1,2,34,3,4,23,2,3,1,0)
print(t1.index(1))

# Demonstration of immutability of tuple as similar to string.

s1 = "Hello World"
s2 = s1.replace("Hello", "Hi")
print(f"s1 variable value is not changed: {s1}. Only new string got created and stored in s2 variable: {s2}")
