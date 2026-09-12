N = int(input())
c = int(input())
p = int(input())
if p <= N:
    print(c)
else:
    a = p - N
    c += a * 5
    print(c)
