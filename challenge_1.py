import math 

side1 = int(input("Enter side 1 of triangle: "))
side2 = int(input("Enter side 2 of triangle: "))
side3 = int(input("Enter side 3 of triangle: "))

semi_perim = (side1 + side2 + side3)/2
print(semi_perim)

area = math.sqrt
(semi_perim * (semi_perim-side1) * (semi_perim-side2) * (semi_perim-side3))

print(area)