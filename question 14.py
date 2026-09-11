command = input().strip()

match command:
    case "RED":
        print("Stop")
    case "YELLOW":
        print("Wait")
    case "GREEN":
        print("Go")
    case _:
        print("Invalid signal")
