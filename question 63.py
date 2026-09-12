x = int(input())
y = int(input())
z = int(input())
if x == y and x == z and y == z:
    print("Equilateral")
elif (x == y) or (y == z) or (z == x):
    print("Isosceles")
else:
    print("Scalene")
