amount = float(input("Order amount: ")) 
zone = input("Zone: ").upper()
if amount >= 1000:
    if zone == "LOCAL" or "CITY":
        print("charges: 0.00")
    elif zone == "OUTSIDE":
        print("Charges: 120.00")   
elif amount < 1000:
    if zone == "LOCAL":
        print("charges: 30.00")
    elif zone == "CITY":
        print("charges: 60.00")
    elif zone == "OUTSIDE":
        print("charges: 120.00")
else:
    print("Invalid zone")
