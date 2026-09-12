n = int(input())
m = int(input())
for i in range(n, m+1):
    if i % 4 == 0 and i % 6 == 0:
        print(i)
        break
print("Not Found")
