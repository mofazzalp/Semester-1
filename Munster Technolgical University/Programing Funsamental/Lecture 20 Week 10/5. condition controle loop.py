import turtle

radius = int(input("Enter a radius number "))
while radius >= 0:
    turtle.circle(radius)
    radius -= 5