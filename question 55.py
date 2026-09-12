username = input()
for user in username:
    if not ('a' <= user <= 'z' or 'A' <= user <= 'Z' or '0' <= user <= '9'):
        print("Invalid")
        break
else:
    print("Valid")
