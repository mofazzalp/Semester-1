# author : Mofazzal Hossain
# Description : Turtle

# turtle module

import turtle

menu = f"Welcome, {""}" \
       "\n\t 1: Circle" \
       "\n\t 2: Square" \
       "\n\t 3: rectangle" \
       "\n ==> "

option = int(input(menu))

if option == 1:
    turtle.circle(100)
    print("Circle") # circle print on python console
elif option == 2:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    print("Square")
elif option == 3:
    print("rectangle")
else:
    print("Invalid Selection")

turtle.done()


"""
menu = f""
print(menu)
option 
"""