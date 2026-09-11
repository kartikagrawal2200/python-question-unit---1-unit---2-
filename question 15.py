shape = input().lower()
match shape:
    case "triangle":
        base = float(input("Enter base length: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area of triangle: {area}")
    case "square":
        side = float(input("Enter side length: "))
        area = side ** 2
        print(f"Area of square: {area}")
    case "rectangle":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        area = length * breadth
        print(f"Area of rectangle: {area}")
    case _:
        print("Invalid shape")
