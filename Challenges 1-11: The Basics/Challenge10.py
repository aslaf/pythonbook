"""
010
There are 2,204 pounds in a kilogram. Ask the
user to enter a weight in kilograms and convert it
to pounds.
"""

kilo = int(input("Enter your weight in kilograms: "))

lbs = 2.204 * kilo

print("That is", round(lbs, 2), "pounds")