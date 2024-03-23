"""
029
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two decimal places
"""

import math

num = int(input("Enter any number over 500: "))
answer = math.sqrt(num)

print("The square root of", num, "is", round(answer, 2))