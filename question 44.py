a = int(input())
b = int(input())
sum = 0
for i in range(a, b+1):
    if i % 4 == 0 or i % 6 == 0:
        continue
    sum += i
print(sum)
