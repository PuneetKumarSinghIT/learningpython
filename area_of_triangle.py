"""
parameter of triangle = a+b+c/2
area = sqrt(s * (s-a) * (s-b) * (s-c))
"""

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("The area of the triangle is:", round(area,2))