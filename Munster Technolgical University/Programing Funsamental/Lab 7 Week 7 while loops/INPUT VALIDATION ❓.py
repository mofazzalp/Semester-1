# Author : Mofazzal Hossain
# Description : INPUT VALIDATION ❓

age = -1
while age <= 0:
    try:
        age = int(input("Invalid age \nEnter Your Age Again (inside try) : "))
    except ValueError:
        age = int(input(f"You Entered string  please enter integer (outside try)"))

print("Valid Number ")
