# author : Mofazzal Hossain
# description : Cinema with Menu :
menu = "1. Morning. € 5.00" \
       "\n2. Afternoon. € 8.00" \
       "\n3. Evening €12.00" \
       "\nEnter your choice >>: "
choose = int(input(menu))
if choose == 1:
    name = input("Name >>: ")
    period = "Morning"
    TICKET_COST = 5.00
    group = int(input("No in the group >>: "))
    print(f"Name Of Booking:{' ' * 5} {name}")
    print(f"Time Period: {' ' * 5} {period} ")
    print(f"Cost of {period} Ticket €{TICKET_COST}")
    print(f"Size of Group {' ' * 7} {group}")
    price = group * TICKET_COST
    if name.startswith("C") and "nn" in name or len(name) == 4:
        final_price = "free"
        print(f"Price charged: {' ' * 5} €{final_price} ")
    else:
        if 5 <= group <= 9:
            discount = 10 / 100
            final_price = price - price * discount
            print(f"Discount applied: {' ' * 5} 10% ")
        elif group >= 10:
            discount = 20 / 100
            print(f"Discount applied: {' ' * 5} 20% ")
            final_price = price - price * discount
        else:
            final_price = price
        print(f"Price charged: {' ' * 5} €{final_price} ")

    if group == 1:
        print("Enjoy a free coffee on the house.")

if choose == 2:
    name = input("Name >>: ")
    period = "Afternoon"
    TICKET_COST = 8.00
    group = int(input("No in the group >>: "))
    print(f"Name Of Booking:{' ' * 5} {name}")
    print(f"Time Period: {' ' * 5} {period} ")
    print(f"Cost of {period} Ticket €{TICKET_COST}")
    print(f"Size of Group {' ' * 5} {group}")
    price = group * TICKET_COST
    if name.startswith("C") and "nn" in name or len(name) == 4:
        final_price = "free"
        print(f"Price charged: {' ' * 5} €{final_price} ")
    else:
        if 5 <= group <= 9:
            discount = 10 / 100
            final_price = price - price * discount
            print(f"Discount applied: {' ' * 5} 10% ")
        elif group >= 10:
            discount = 20 / 100
            print(f"Discount applied: {' ' * 5} 20% ")
            final_price = price - price * discount
        else:
            final_price = price
        print(f"Price charged: {' ' * 5} €{final_price} ")

    if group == 1:
        print("Enjoy a free coffee on the house.")

if choose == 3:
    name = input("Name >>: ")
    period = "Evening"
    TICKET_COST = 12.00
    group = int(input("No in the group >>: "))
    print(f"Name Of Booking:{' ' * 5} {name}")
    print(f"Time Period: {' ' * 5} {period} ")
    print(f"Cost of {period} Ticket €{TICKET_COST}")
    print(f"Size of Group{' ' * 5} {group}")
    price = group * TICKET_COST
    if name.startswith("C") and "nn" in name or len(name) == 4:
        final_price = "free"
        print(f"Price charged: {' ' * 5} €{final_price} ")
    else:
        if 5 <= group <= 9:
            discount = 10 / 100
            final_price = price - price * discount
            print(f"Discount applied: {' ' * 5} 10% ")
        elif group >= 10:
            discount = 20 / 100
            print(f"Discount applied: {' ' * 5} 20% ")
            final_price = price - price * discount
        else:
            final_price = price
        print(f"Price charged: {' ' * 5} €{final_price} ")

    if group == 1:
        print("Enjoy a free coffee on the house.")


