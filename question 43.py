words = input().lower()
vowels = "aeiou"
for i in words:
    if i in vowels:
        continue
    print(i,end="\n")
