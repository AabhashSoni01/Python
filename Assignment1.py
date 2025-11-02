# A wire is the form of Arc at an angle of 60 degrees and the radius of the arc is 42. 
# The wire is converted into a square. Find the area of the square.

import math

degrees = 60

radius = 42

arc_length = (degrees / 360) * 2 * math.pi * radius

perimeter_square = arc_length

side_square = perimeter_square / 4

area_square = side_square ** 2

print(f"1. Length of the wire (Arc length): {arc_length:.5f} units")
print(f"2. Side length of the square: {side_square:.5f} units")
print(f"3. Area of the square: {area_square:.5f} square units")