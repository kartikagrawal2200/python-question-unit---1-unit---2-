words = input()
for i in words:
    if i.isdigit():
        continue
    print(i,end="")
