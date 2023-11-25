# Author : Mofazzal Hossain
# Description : WRITING TO A FILE IN A LOOP

newfile = open("presents.txt", "w")

while True:
    try:
        user_number = int(input(" Enter the number of people for whom they must buy presents for Christmas:  "))
        break
    except ValueError:
        print("Enter the number of people for whom they must buy presents for Christmas as a Integer number :  >>")
STRING_accumulator = ''

NAME = "Name"
BUDJET_Title = "Budget"

try:
    for person in range(user_number):
        name = input(f"Enter {person + 1} person name ")
        while True:
            try:
                budget = int(input(f"Enter {person + 1} person Budget  "))
                break
            except ValueError:
                print("Please Enter any amount of budget as an Integer number ")
        STRING_accumulator += F"{name:20} {budget:,.2f}\n"

except ValueError:
    print("Enter Budget as integer Value ")
print(f"{NAME:20} €{BUDJET_Title}", file=newfile)
print("-" * 30, file=newfile)
print(f"{STRING_accumulator}", file=newfile)
