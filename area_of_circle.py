import math

def calculate_area(radius):
    area = math.pi * radius * radius
    return area

radii = [1, 5, 10]

for radius in radii:
    area = calculate_area(radius)
    print("The area of a circle with radius " + str(radius) + " is: " + str(area))
