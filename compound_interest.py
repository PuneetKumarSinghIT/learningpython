"""
This module calculates compound interest based on the formula:
Amount = Principal * (1 + Rate/100) ** Time - Principal
Compound Interest = Amount - Principal
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print("The amount after", time, "years is:", round(amount, 2))
print("The compound interest is:", round(compound_interest, 2))