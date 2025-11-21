import math

degrees = 60
radius = 42
arc_length = (degrees / 360) * 2 * math.pi * radius
perimeter = arc_length
side= perimeter / 4
area = side ** 2

print(f"Area of the square: {area:.5f}")