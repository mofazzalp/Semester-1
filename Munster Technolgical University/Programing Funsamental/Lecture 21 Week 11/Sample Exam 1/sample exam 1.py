# author : Mofazzal
# description : sample question 1

Ground_Floor = 10.50
Balcony_Price = 12.80
Box_Price = 15.50

space = ''
price = 0
user_name = input("Enter Name: ")

choose = int(input(f"Enter Seating Location: (1.Ground Floor 2.Balcony 3.Box): "))
parking_require = input("Will you need a car parking space (y/n):")
tickets = int(input('Number tickets required: '))
if parking_require == 'y':
    m = '(Parking Required)'
else:
    m = '(no Required )'

if choose == 1:
    price = Ground_Floor
    space = "Ground Floor"
elif choose == 2:
    space = "Balcony"
    price = Balcony_Price
elif choose == 3:
    space = "Box"
    price = Box_Price

print("\n")
print("Thank you for booking, here are your booking details:")
print("CIT Pantomime Booking Details for Harold Grange")
print("-" * 50)
if tickets <= 10:
    discount_price = price * tickets
    print(f"{space} {tickets} People  €{discount_price} {m}")
elif tickets > 10:
    discount_price = price * (tickets - 1)
    print(f"{space} {tickets} People  €{discount_price:,.2f} {m}")
