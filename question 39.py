number = list(map(int, input().split()))
sum = 0
for num  in number:
    if num == 0:
        break
    sum += num
print(sum)
