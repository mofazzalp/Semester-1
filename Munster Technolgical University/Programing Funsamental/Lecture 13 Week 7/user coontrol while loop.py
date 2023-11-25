# Author : Mofazzal Hossain
# Description : Loop : while : user control
# Date : 06/11/2023
print("Please enter the number you want to add together")
number = int(input("Please enter a number (0 to finish) : "))
accumulator = 0

while number != 0:  # part of loop condition
    accumulator += number
    print(f"You entered {number} - thank you")
    number = int(input("Enter a number t (0 to finish) :  "))
    print(f"sum of your numbers {accumulator}")
print(f"sum of your numbers {accumulator}")
print("Loop Finished")
