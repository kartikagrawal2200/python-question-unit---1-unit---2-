number = list(map(int, input().split()))
target = int(input()) 
for num in number:
    if num == target:
        print("Found")
        break
else:
    print("Not Found")
