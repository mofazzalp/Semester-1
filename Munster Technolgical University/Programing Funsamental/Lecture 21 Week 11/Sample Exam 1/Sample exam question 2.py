# author : Mofazzal
# description : sample question 2

Ground_PRICE = 10.50
Balcony_PRICE = 12.80
BOX_PRICE = 15.50

summary = open("summary.txt", "a")
space = ''
price = 0
loop_number = 0
discount_price = 0
tickets_total = 0

TOTAL_NAME = ''
PARKING_Status = ''
PARKING_TOTAL = 3

booking = int(input("How many bookings are there? "))
for i in range(booking):
    loop_number += 1
    print("\n")
    print("CIT Pantomime Booking")
    print("-"*22)
    user_name = input(f"Enter a name for this booking #{loop_number}:  ")
    choose = int(input(f"Enter Seating Location: (1.Ground Floor 2.Balcony 3.Box): "))
    tickets = int(input('Number of people in your group: '))
    tickets_total += tickets
    if PARKING_TOTAL > 0:
        parking_require = input("Will you need a car parking space (y/n):").lower()
        if parking_require == 'y':
            PARKING_Status = '(Parking Required)'
            PARKING_TOTAL -= 1
        elif parking_require == 'n':
            PARKING_Status = '(no Required )'
    elif PARKING_TOTAL >= -1:
        PARKING_Status = '(no Required )'

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
    print("Thank you for booking, here are your booking details:\n")
    print(f"CIT Pantomime Booking Details for {user_name}")
    TOTAL_NAME += f"{user_name:15s} {space:15s} {tickets:3d} \n"

    if tickets <= 10:
        discount_price = price * tickets
        print(f"{space} {tickets} People  €{discount_price:,.2f} {PARKING_Status}")
    elif tickets > 10:
        discount_price = price * (tickets - 1)
        print(f"{space} {tickets} People  €{discount_price:,.2f} {PARKING_Status}")

print("Summary of Bookings",file=summary)
print("="*20,file=summary)
print(TOTAL_NAME,file=summary)
print(f"Total no. of People:  {tickets_total:10d}",file=summary)
summary.close()
