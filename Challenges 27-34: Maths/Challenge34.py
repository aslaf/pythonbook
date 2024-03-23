"""
034
Display the following message:
1. Square
2. Triangle

Enter a number:
If the user enters 1, then it should ask them for the length of one of its sides and display the
area. If they select 2, it should ask for the base and height of the triangle and display the area. If
they type in anything else, it should give them a suitable error message.
"""
# import math
print("1. Square")
print("2. Triangle")

num = int(input("Enter a number: "))

if num == 1:
    length = int(input("Enter length: "))
    area = length ** 2
    print("Area of square is", area)
elif num == 2:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Area of rectangle is", area)
else:
    print("Incorrect option chosen")
