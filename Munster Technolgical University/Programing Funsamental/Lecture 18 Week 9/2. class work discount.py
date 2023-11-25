# Author : Mofazzal Hossain
# description : 10% discount on  car price

import datetime
DISCOUNT = 10/100

EXPENSIVE_PRICE = 0
EXPENSIVE_CAR = ''
current_year = datetime.date.today().year

f = open("cars.txt", "r")
for line in f:
    line = line.rstrip() # only remove space from the right side
    line = line.split(sep=',')
    make = line[0]
    model = line[1]
    year = int(line[2])
    fuel_type = line[3]
    price = float(line[4])
    print(line)
    discount = price - (price*DISCOUNT)
    age = current_year - year
    print(f"{make} {model} {year} {fuel_type} €{discount:,.2f}")
    print(f"{age} year old {make} {model} ({fuel_type}) €{discount:,.2f} ")

    if price > EXPENSIVE_PRICE:
        EXPENSIVE_PRICE = price
        EXPENSIVE_CAR = f"{make} {model}"


f.close()
print(f"The {EXPENSIVE_CAR} was the most expensive ")