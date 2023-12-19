# Author : Mofazzal Hossain
# Description : Question 1

parking_space = ''

Ground_Floor = 10.50
Balcony = 12.80
Box = 15.00

total_cost = 0
space_name = ''

user_name = input("Enter Name: ")
space_location = int(input("Enter Seating Location: (1.Ground Floor 2.Balcony 3.Box): "))
parking_ask = input("Will you need a car parking space (y/n): ")
tickets_ask = int(input("Number tickets required:  "))

if parking_ask == 'y':
    parking_space = '(Parking Required)'
elif parking_ask == 'n':
    parking_space = '(Parking Not Required)'

print("Thank you for booking, here are your booking details: \n")
print(f"CIT Pantomime Booking Details for {user_name}")
print("-"*48)

if space_location == 1:
    space_name = "Ground Floor"
    if tickets_ask <= 10:
        total_cost = tickets_ask * Ground_Floor
    elif tickets_ask > 10:
        total_cost = (tickets_ask - 1) * Ground_Floor
elif space_location == 2:
    space_name = "Balcony "
    if tickets_ask <= 10:
        total_cost = tickets_ask * Balcony
    elif tickets_ask > 10:
        total_cost = (tickets_ask - 1) * Balcony
elif space_location == 3:
    space_name = "Box"
    if tickets_ask <= 10:
        total_cost = tickets_ask * Box
    elif tickets_ask > 10:
        total_cost = (tickets_ask - 1) * Box

print(f"{space_name}, {tickets_ask} People, €{total_cost} {parking_space}")