code = input("Enter: ")
for i in code:
    if not (i <= '9' and i >= '0'):
        print("Not Valid")
        break
else:
    print("Valid")
