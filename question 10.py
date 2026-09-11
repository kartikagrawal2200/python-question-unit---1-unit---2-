username = input("Username: ")
pin = int(input("PIN: "))
if username == "admin":
    if pin == 2468:
        print("Access Granted")
    else:
        print("Wrong PIN")
else:
    print("Unknown User")
