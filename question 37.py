number = list(map(int, input().split())) 
for num in number: 
    if num < 0: 
        print(num)
        break  
print("No negative")
