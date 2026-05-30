"""
This module provides a dictionary implementation using a hash table.
A dictionary is an unordered collection of key-value pairs.
"""
groceries = {'milk': 60, 'biscuits': 20, 'bread': 30, 'rice': 90}
print(f"Groceries: {groceries}")
print(f"Price of milk: {groceries['milk']}")
print(f"Price of bread: {groceries['bread']}")
print(f"Price of rice: {groceries['rice']}")
print(f"datatype of groceries variable: {type(groceries)}")
print(f"Length of groceries dictionary: {len(groceries)}")
groceries['eggs'] = 50
print(f"Groceries after adding eggs: {groceries}")
groceries['milk'] = 65
print(f"Groceries after updating milk price: {groceries}")
print(f"Keys in groceries: {groceries.keys()}")
print(f"Values in groceries: {groceries.values()}")
print(f"Items in groceries: {groceries.items()}")