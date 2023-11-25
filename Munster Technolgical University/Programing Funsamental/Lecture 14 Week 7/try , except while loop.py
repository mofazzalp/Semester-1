# Author : Mofazzal Hossain
# Description : try except

user_grade = -1
while not (0 <= user_grade <= 100):

    try:
        user_grade = float(input("Enter the Grade "))
    except ValueError :
        print("You need to enter an integer value")

print(f"Your grade was {user_grade}")