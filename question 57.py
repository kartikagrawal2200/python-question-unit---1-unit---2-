n = int(input())
if n <= 3:
    print("Should be greater then 3")
else:
    is_composite = False
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            is_composite = True
    if is_composite:
        print("Eligible")
    else:
        print("Not eligible")
