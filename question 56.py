x = int(input())
y = int(input())

if x == 0 or y == 0:
    print("value must be nonzero")
else:
    a = abs(x)
    b = abs(y)
    while b != 0:
        a, b = b, a % b
    print(f"gcd: {a}")
