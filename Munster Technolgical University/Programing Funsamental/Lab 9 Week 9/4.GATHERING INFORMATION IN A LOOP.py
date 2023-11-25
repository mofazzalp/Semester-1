# Author : Mofazzal Hossain
# Description : GATHERING INFORMATION IN A LOOP
newfile = open("m.txt", "w")

user_number = int(input(" Enter the number of people for whom they must buy presents for Christmas."))

STRING_accumulator = ''
NAME = "Name"
BUDJET_Title = "Budget"

try:
    for person in range(user_number):
        name = input(f"Enter {person + 1} person name ")
        budget = int(input(f"Enter {person + 1} person Budget  "))
        STRING_accumulator += F"{name:20} {budget:,.2f}\n"

except ValueError:
    print("Enter Budget as integer Value ")
print(f"{NAME:20} €{BUDJET_Title}", file=newfile)
print("-" *30,file=newfile)
print(f"{STRING_accumulator}", file=newfile)
