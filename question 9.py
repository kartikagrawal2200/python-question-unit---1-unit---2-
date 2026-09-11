u = int(input())
if u <= 100:
    u1 = u * 2
    print(u1)
elif u > 100 and u <= 200:
    u1 = 100 * 2 + (u - 100) * 3
    print(u1)
elif u > 200:
    u1 = 100 * 2 + 100 * 3 + (u - 200) * 5
    print(u1)
