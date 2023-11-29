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
    radius = int(input("Enter the circle radius "))
    turtle.circle(radius)
    print("Circle") # circle print on python console
elif option == 2:
    side = int(input("Enter th elen of each side "))
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)
    print("Square")
elif option == 3:
    height = int(input("Enter the height "))
    width = int(input("Enter the width "))
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    print("rectangle")
else:
    print("Invalid Selection")

turtle.done()


"""
menu = f""
print(menu)
option 
"""