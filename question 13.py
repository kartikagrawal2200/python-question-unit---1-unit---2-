marks = int(input())
match marks:
    case m if m >= 90:
        print("A")
    case m if m >= 80:
        print("B")
    case m if m >= 70:
        print("C")
    case m if m >= 60:
        print("D")
    case _:
        print("F")
