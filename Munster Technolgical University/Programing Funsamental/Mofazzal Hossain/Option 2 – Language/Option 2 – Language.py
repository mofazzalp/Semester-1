first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")

menu = f"Welcome, {first_name}" \
       "\n\t 1: Maths" \
       "\n\t 2: Irish" \
       "\n ==> "

choose = int(input(menu))

if choose == 2:
    current_level = int(input(f"{first_name}, what is your current level? "))
    if current_level == 1:
        print()
