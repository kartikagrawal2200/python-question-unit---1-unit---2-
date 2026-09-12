balance, withdrawal = map(int, input().split())
if withdrawal <= 0:
    print("Invalid amount")
elif withdrawal % 100 != 0:
    print("Amount must be multiple of 100")
elif withdrawal > balance:
    print("Insufficient balance")
else:
    new_balance = balance - withdrawal
    print(f"new balance: {new_balance}")
