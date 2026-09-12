Salary = int(input())
Gender = input().upper()
if Salary > 10000:
    if Gender == 'M':
        bonus = Salary * 0.05
        salary = Salary + bonus
        print(f"{bonus:.2f}")
        print(f"{salary:.2f}")
    elif Gender == 'F':
        bonus =  Salary * 0.1
        Salary == Salary + bonus
        print(f"{bonus:.2f}")
        print(f"{Salary:.2f}")
elif Salary < 10000:
    if Gender == 'M':
        bonus = Salary * 0.05 + Salary * 0.02
        salary = Salary + bonus
        print(f"{bonus:.2f}")
        print(f"{salary:.2f}")
    elif Gender == 'F':
        bonus = Salary * 0.1 + Salary * 0.02
        salary = Salary + bonus
        print(f"{bonus:.2f}")
        print(f"{salary:.2f}
