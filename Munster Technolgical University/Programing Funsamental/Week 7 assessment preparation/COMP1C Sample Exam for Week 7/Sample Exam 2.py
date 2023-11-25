# author : Mofazzal Hossain
# Purpose : Sample Exam : 2
units = int(input("Enter How many Units You Purchased "))
unit_price = float(input("Enter the price "))
total = units * unit_price
if 1 <= units <= 49:
    if 0.00 <= unit_price <= 10.00:
        print(f"{units} Units at €{unit_price} Cost {total}")
    elif unit_price >= 10.01:
        discount = total - total * (5 / 100)
        print(f"{units} Units at €{unit_price} Cost {total}")
        print(f"{units} Units at €{unit_price} Cost {discount}")
elif 50 <= units <= 99:
    if 0.00 <= unit_price <= 10.00:
        discount = total - total * (12 / 100)
        print(f"{units} Units at €{unit_price} Cost {total}")
        print(f"{units} Units at €{unit_price} Cost {discount}")
    elif unit_price >= 10.01:
        discount = total - total * (18 / 100)
        print(f"{units} Units at €{unit_price} Cost {total}")
        print(f"{units} Units at €{unit_price} Cost {discount}")
elif units >= 100:
    if 0.00 <= unit_price <= 10.00:
        discount = total - total * (21 / 100)
        print(f"{units} Units at €{unit_price} Cost {total}")
        print(f"{units} Units at €{unit_price} Cost {discount}")
    elif unit_price >= 10.01:
        discount = total - total * (32 / 100)
        print(f"{units} Units at €{unit_price} Cost {total}")
        print(f"{units} Units at €{unit_price} Cost {discount}")
