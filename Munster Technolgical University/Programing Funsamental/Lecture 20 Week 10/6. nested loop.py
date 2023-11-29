# many square
import turtle
side = int(input("Enter the side length "))
while side >= 0:
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)
        # side -= 5
    side -= 5 # this line depends on side of the side