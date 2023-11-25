# Author : MOfazzla Hossain
# description :reading file from user

f = open("cars.txt", "r") # default access mode is "r"

for line in f:
    line = line.rstrip() # only remove space from the right side
    line = line.split(sep=',')
    make = line[0]
    model = line[1]
    year = int(line[2])
    fuel_type = line[3]
    price = float(line[4])
    print(line)
    print(f"{make} {model} {year} {fuel_type} €{price:,.2f}")


f.close()
