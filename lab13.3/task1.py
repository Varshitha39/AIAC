from math import pi

def area_rectangle(width, height):
    return width * height

def area_square(side):
    return side * side

def area_circle(radius):
    return pi * radius * radius

def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return area_rectangle(x, y)
    elif shape == "square":
        return area_square(x)
    elif shape == "circle":
        return area_circle(x)

if __name__ == "__main__":
    print("Rectangle (5 x 3):", calculate_area("rectangle", 5, 3))
    print("Square (side 4):", calculate_area("square", 4))
    print("Circle (radius 2):", calculate_area("circle", 2))
    