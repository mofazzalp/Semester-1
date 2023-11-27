# Author : Mofazzal Hossain
# Description :  Assignment


import random

operators = ['+', '-']

user_option = ''
correct_answers = 0
questions = ''
calculation_question = 0

first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")

menu = f"Welcome, {first_name}" \
       "\n\t 1: Maths" \
       "\n\t 2: Irish" \
       "\n ==>"
choose = int(input(menu))
if choose == 1:
    option = int(input(f"{first_name}, how many questions You want to answer ? "))
    while not (5 <= option <= 25):
        option = int(input("Enter  (5 - 25)"))
        user_option += f"{option}"
        break
print(user_option)
if choose == 1:
    option = int(input(f"{first_name}, how many questions do you want to answer? "))

    while not (5 <= option <= 25):
        option = int(input("Enter (5 - 25): "))

    user_option += f"{option}"

print(user_option)
