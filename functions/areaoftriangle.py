def perimeter_of_triangle(a, b, c):
    perimeter_of = a + b + c
    return perimeter_of

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area_of_ = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area_of_

a = 23
b = 35
c = 54

perimeter = perimeter_of_triangle(a, b, c)
area = area_of_triangle(a, b, c)

print("This is the perimeter of the triangle:", perimeter)
print("This is the area of the triangle:", area)



#OUTPUT
# This is the perimeter of the triangle: 112
# This is the area of the triangle: 278.5964823898536