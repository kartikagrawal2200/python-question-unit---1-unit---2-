n = int(input())
d = int(input())
for i in range(2, n):
    if n % i == 0 and i == d:
        print("Target divisor found")
        break
else:
    print("Target divisor not found")
