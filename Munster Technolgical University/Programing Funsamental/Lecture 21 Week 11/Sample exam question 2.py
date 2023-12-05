# author : Mofazzal
# description : sample question 2

Ground_PRICE = 10.50
Balcony_PRICE = 12.80
BOX_PRICE = 15.50

summary = open(" summary.txt", "a")
space = ''
price = 0
loop_number = 0
discount_price = 0
tickets_total = 0


booking = int(input("How many bookings are there? "))
for i in range(booking):
    loop_number += 1

    user_name = input(f"Enter a name for this booking #{loop_number}:  ")
    choose = int(input(f"Enter Seating Location: (1.Ground Floor 2.Balcony 3.Box): "))
    parking_require = input("Will you need a car parking space (y/n):")
    tickets = int(input('Number tickets required: '))
    tickets_total += tickets

    if parking_require == 'y':
        m = '(Parking Required)'
    else:
        m = '(no Required )'

    if choose == 1:
        space = "Ground Floor"
        price = Ground_PRICE
    elif choose == 2:
        space = "Balcony"
        price = Balcony_PRICE
    elif choose == 3:
        space = "Box"
        price = BOX_PRICE

    print("\n")
    print("CIT Pantomime Booking")
    print("-"*22)
    print("Thank you for booking, here are your booking details:")
    print(f"CIT Pantomime Booking Details for {user_name}")
    print("-" * 50)
    if tickets <= 10:
        discount_price = price * tickets
        print(f"{space} {tickets} People  €{discount_price:,.2f} {m}")
    elif tickets > 10:
        discount_price = price * (tickets - 1)
        print(f"{space} {tickets} People  €{discount_price:,.2f} {m}")

    print("Summary of Bookings",file=summary)
    print("="*20)
    print(f"{user_name:10s} {space:10s} {tickets}",file=summary)
    print(f"Total no. of People: 10s {tickets_total}",file=summary)
summary.close()