"""
This module calculates simple interest based on the formula:
Simple Interest = (Principal * Rate * Time) / 100
"""

principle = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principle * rate * time) / 100
print("The simple interest is:", round(simple_interest, 2))