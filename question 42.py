number = list(map(int, input().split()))
sum = 0
for i in number:
    if i < 0:
        continue
    sum += i
print(sum)  
