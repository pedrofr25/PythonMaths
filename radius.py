import math

radius = int(input("Enter the radius of your circle:"))

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print ("The circunference of a circle with the radius", radius, "is:%.2f" \
%circumference, "and the area is:%.2f" %area)
