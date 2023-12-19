# Author : Mofazzal Hossain
# Description : Question 2

parking_space = ''
PARKING_available = 3

Ground_Floor = 10.50
Balcony = 12.80
Box = 15.00

person_name = ''
tickets = 0

total_cost = 0
space_name = ''
total_people = 0
summary = ''

Ground_seat_total = 0
Balcony_seat_total = 0
Box_seat_total = 0
most_expensive_cost = 0
price = 0
Discount_price = 0
name = ''
most_expensive_person = ''

log = open("summary.txt", "a")

loop = int(input("How many bookings are there? "))
for number in range(loop):
    print("CIT Pantomime Booking")
    print("-" * 22)

    user_name = input(f"Enter a name for this booking #{number + 1}: ")
    person_name = user_name
    space_location = int(input("Enter Seating Location: (1.Ground Floor 2.Balcony 3.Box): "))
    if 0 < PARKING_available <= 3:
        parking_ask = input("Will you need a car parking space (y/n): ")
        if parking_ask == 'y':
            parking_space = '(Parking Required)'
            PARKING_available -= 1
        elif parking_ask == 'n':
            parking_space = '(Parking Not Required)'
    else:
        parking_space = ''
        parking_ask = 'No'
    tickets_ask = int(input("Number of people in your group: "))
    total_people += tickets_ask
    tickets = tickets_ask

    print("Thank you for booking, here are your booking details: \n")
    print(f"CIT Pantomime Booking Details for {user_name}")
    print("-" * 48)

    if space_location == 1:
        space_name = "Ground Floor"
        price = Ground_Floor
        Ground_seat_total = tickets_ask
        summary += f"{person_name:<11s} {space_name:13} {tickets_ask:>8d}\n"
        if tickets_ask <= 10:
            total_cost = tickets_ask * Ground_Floor
        elif tickets_ask > 10:
            total_cost = (tickets_ask - 1) * Ground_Floor
    elif space_location == 2:
        space_name = "Balcony "
        price = Balcony
        Balcony_seat_total = tickets_ask
        summary += f"{person_name:<11s} {space_name:13} {tickets_ask:>8d}\n"
        if tickets_ask <= 10:
            total_cost = tickets_ask * Balcony
        elif tickets_ask > 10:
            total_cost = (tickets_ask - 1) * Balcony
    elif space_location == 3:
        space_name = "Box"
        price = Box
        Box_seat_total = tickets_ask
        summary += f"{person_name:<11s} {space_name:13} {tickets_ask:>8d}\n"
        if tickets_ask <= 10:
            total_cost = tickets_ask * Box
        elif tickets_ask > 10:
            total_cost = (tickets_ask - 1) * Box

    print(f"{space_name}, {tickets_ask} People, €{total_cost} {parking_space}")

print("Summary of Bookings", file=log)
print("=" * 24, file=log)
print(summary, file=log)
print(f"Total no. of People: {total_people:>13d}", file=log)

log.close()
