# Author : Mofazzal Hossain
# Description :  Assignment


import random

operators = ['+', '-']
SPECIAL_CHARACTER_CORRECT = u'\u2713'
SPECIAL_CHARACTER_WRONG = u'\u274c'

user_option = 0
correct_answers = 0
question_no = 0
questions1 = ''
questions2 = ''
calculation_question = 0

first_name = input("What is your first name? ")

menu = f"Welcome, {first_name}" \
       "\n\t 1: Maths" \
       "\n\t 2: Irish" \
       "\n ==> "

choose = int(input(menu))

if choose == 1:
    option = int(input(f"{first_name}, how many questions? "))

    while not (5 <= option <= 25):
        option = int(input("Enter (5 - 25): "))

    user_option = option  # f"{option}"
    for i in range(option):
        question_no += 1
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        operator = random.choice(operators)
        if num1 > num2 or num1 == num2:
            question = f"{num1} {operator} {num2}"
            calculation_question = question
            print()
        elif num2 > num1:
            question = f"{num2} {operator} {num1}"
            calculation_question = question
            print()
print(calculation_question)