# Author : Mofazzal Hossain
# Description : checking how may times a ball bounces
# Date : 06/11/2023

height = float(input("Enter the Height of ball "))
i = 0.01  # initialised before the loop
iteration = 1

while height >= i:  # part of loop condition
    print(f"height: {height}, bounce iteration : {iteration} ")
    iteration = iteration + 1  # changes during the loop
    height = height/2
