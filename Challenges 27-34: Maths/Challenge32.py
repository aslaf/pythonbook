"""
032
Ask for the radius and the depth of a cylinder
and work out the total volume (circle area*depth) rounded to three decimal places.
"""

import math
radius = int(input("Enter radius of a cylinder: "))
depth = int(input("Enter depth: "))

area = math.pi * (radius ** 2)
volume = area * depth

print(round(volume, 3))