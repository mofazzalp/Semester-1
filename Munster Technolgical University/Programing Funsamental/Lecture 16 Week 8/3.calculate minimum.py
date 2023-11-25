# Author: Mofazzal Hossain
# Description: calculate minimum

lowest = 1000

for iteration in range(5):
    while True:
        try:
            number = int(input(f"Enter {iteration+1} number: "))
            break
        except ValueError:
            print("Please enter your number as an integer.")

    if number < lowest:
        lowest = number

print(f"The lowest number is {lowest}.")


"""
# Author: Mofazzal Hossain
# Description: calculate minimum # using while loop

lowest = 1000
iteration = 0
while iteration < 5:
    iteration += 1
    while True:
        try:
            number = int(input(f"Enter {iteration} number: "))
            break
        except ValueError:
            print("Please enter your number as an integer.")

    if number < lowest:
        lowest = number

print(f"The lowest number is {lowest}.")

"""