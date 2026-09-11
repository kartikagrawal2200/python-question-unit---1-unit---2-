words = list(map(str, input("Enter words separated by space: ").split()))

count = 0
for char in words:
   print(f"Word: {char}, Length: {len(char)}")
   count += 1
print("count:", count)
