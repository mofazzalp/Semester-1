# Author : Mofazzal Hossain
# Description :  Assignment


import random

operators = ['+', '-']
SPECIAL_CHARACTER_CORRECT = u'\u2713'
SPECIAL_CHARACTER_WRONG = u'\u274c'

user_option = 0
correct_answers = 0
questions1 = ''
questions2 = ''
calculation_question = 0

user_answer1 = ''
answer1 = ''

first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")

menu = f"Welcome, {first_name}" \
       "\n\t 1: Maths" \
       "\n\t 2: Irish" \
       "\n ==> "

choose = int(input(menu))

if choose == 1:
    option = int(input(f"{first_name}, how many questions? "))

    while not (5 <= option <= 25):
        option = int(input("Enter (5 - 25): "))

    user_option += option  # f"{option}"

for question_no in range(user_option):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    operator = random.choice(operators)
    if num1 > num2 or num1 == num2:
        question = f"{num1} {operator} {num2}"
        calculation_question = question
    elif num2 > num1:
        question = f"{num2} {operator} {num1}"
        calculation_question = question
    answer = eval(calculation_question)  # Evaluate the expression to get the correct answer
    # questions = f"(calculation_question, answer))"
    user_answer = int(input(f"{question_no + 1}: {calculation_question} = "))

    user_answer1 += f"{user_answer}"
    answer1 += f"{answer}"
    if user_answer == answer:
        correct_answers += 1
print(user_answer1, answer1)
print(type(user_answer1))


for i in range(user_option):
    if user_answer1[i] == answer1[i]:
        print(f"{i + 1} : {calculation_question}, = {answer1[i]} {SPECIAL_CHARACTER_CORRECT}\n")
    else:
        print(f"{i + 1} : {calculation_question}, = {user_answer1[i]} {SPECIAL_CHARACTER_WRONG} should be {answer1[i]}\n")

average_score = correct_answers / user_option * 100
print(f"{first_name} you got {average_score:.2f}%.")
