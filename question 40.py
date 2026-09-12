password = input()
found = False
for i in password:  
    if i.isdigit():
        print("First digit: ", i)
        found = True
        break
if not found:
    print("Fot found")
