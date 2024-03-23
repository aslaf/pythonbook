"""
027
Ask the user to enter a number with lots of
decimal places. Multiply this number by two and display the answer.
028
Update program 027 so that it will display the answer to
two decimal places.
"""

num = float(input("Enter a number with many decimals: "))

final = num * 2
print(round(final, 2))