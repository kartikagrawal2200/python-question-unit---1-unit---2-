correct_pin = 4321
attempts = 0
max_attempts = 3
while attempts < max_attempts:
   user_input = int(input("Enter PIN: "))
   attempts += 1
    
   if user_input == correct_pin:
      print("Access Granted")
      break
else:
   print("Card Blocked")
