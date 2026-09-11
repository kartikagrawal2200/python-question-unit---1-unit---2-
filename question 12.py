a = int(input())
b = int(input())
c = input()
match a,b,c:
    case a,b,"+":
        print(a + b)
    case a,b,"-":
        print(a - b)
    case a,b,"*":
        print(a * b)
    case a,b,"/":
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero")
    case _:      
        print("Invalid operation")

