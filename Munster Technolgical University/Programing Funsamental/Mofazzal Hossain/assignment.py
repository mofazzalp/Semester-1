# Author : Mofazzal Hossain
# Description :  Assignment

import random
from datetime import datetime
activity_log = open("logs.txt", "a")
custom_format = datetime.now().strftime("%B %d, %Y %H:%M")

operators = ['+', '-']
SPECIAL_CHARACTER_CORRECT = u'\u2713'
SPECIAL_CHARACTER_WRONG = u'\u274c'
user_option = 0
correct_answers = 0

choose = 0
calculation_question = 0
math_question = 0
exam_taken_level = 0
average_score1 = 0

local_correct_ans_count = 0

loop = 0
Count_inConnection = 0
connection1 = ''
word_questions1 = ''

Exam_Name = ''
Math_count = 0
Word_count = 0
local_questions_count = 0

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

while loop == 0:
    exam_taken_level += 1
    menu = f"Welcome, {first_name}" \
           "\n\t 1: Maths" \
           "\n\t 2: Irish" \
           "\n ==> "
    choose = int(input(menu))
    if choose == 1:
        local_correct_ans_count = 0 # reset previous / 1st attempt  answer count
        # 2nd attempt will be count in 61 th line
        Math_count += 1
        Exam_Name = ''# reset previous data
        Exam_Name += f"Math{Math_count}"
        questions1 = ''
        option = int(input(f"{first_name}, how many questions? "))
        Count_inConnection += option  # counting how many times math 1 questions taken. this will be use for final average
        while not (5 <= option <= 25):
            option = int(input("Enter (5 - 25): "))

        user_option = option
        questions1 = ''
        for question_no in range(user_option):
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
            operator = random.choice(operators)
            if num1 > num2 or num1 == num2:
                question = f"{num1} {operator} {num2}"
                calculation_question = question  # send to global variable to access from outside the conditions
            elif num2 > num1:
                question = f"{num2} {operator} {num1}"
                calculation_question = question
            answer = eval(calculation_question)  # Evaluate the expression to get the correct answer
            user_answer = float(input(f"{question_no + 1}: {calculation_question} = "))

            if user_answer == answer:
                local_correct_ans_count += 1  # increase count to show math exam average
                correct_answers += 1  # store to count final average for end of the quiz
                questions1 += f"{question_no + 1} : {calculation_question}, = {answer} {SPECIAL_CHARACTER_CORRECT}\n"
            else:
                questions1 += f"{question_no + 1} : {calculation_question}, = {user_answer} {SPECIAL_CHARACTER_WRONG} should be {answer}\n"

        print(questions1)
        average_score = (local_correct_ans_count / user_option) * 100
        average_score1 = average_score
    if choose == 2:
        Word_count += 1
        Exam_Name = ''  # reset previous data
        Exam_Name += f"Irish{Word_count}"

        current_level = int(input(f"{first_name}, what is your current level? "))
        if current_level == 1:
            connection = open("1.txt", "r")
            connection1 = connection

            word_questions1 = ''
            local_correct_ans_count = 0
            local_questions_count = 0
        elif current_level == 2:
            connection = open("2.txt", "r")
            connection1 = connection

            word_questions1 = ''# reset previous one
            local_correct_ans_count = 0
            local_questions_count = 0
        elif current_level == 3:
            connection = open("3.txt", "r")
            connection1 = connection

            word_questions1 = ''# reset previous one
            local_correct_ans_count = 0
            local_questions_count = 0
        elif current_level == 4:
            connection = open("4.txt", "r")
            connection1 = connection

            word_questions1 = ''# reset previous one
            local_correct_ans_count = 0
            local_questions_count = 0
        elif current_level == 5:
            connection = open("5.txt", "r")
            connection1 = connection

            word_questions1 = ''# reset previous one
            local_correct_ans_count = 0
            local_questions_count = 0
        for line in connection1:
            local_questions_count += 1
            Count_inConnection += 1  # final average count
            line = line.strip()
            line = line.split("=")
            weekdays_count = line[0]
            weekdays = line[1]

            user_answer = input(f"{local_questions_count}: {weekdays_count} = ")
            if user_answer == weekdays:
                correct_answers += 1
                local_correct_ans_count += 1  # local average count
                word_questions1 += f"{local_questions_count} : {weekdays_count}, = {weekdays} {SPECIAL_CHARACTER_CORRECT}\n"
            else:
                word_questions1 += f"{local_questions_count} : {weekdays_count}, = {user_answer} {SPECIAL_CHARACTER_WRONG} should be {weekdays}\n"
        average_score = (local_correct_ans_count / local_questions_count) * 100
        average_score1 = average_score
        print(word_questions1)
        connection1.close()

    if 0 <= average_score1 < 50:
        print(f"{first_name} you got {average_score1:.2f} \U0001F613.")
    elif 50 <= average_score1 < 70:
        print(f"{first_name} you got {average_score1:.2f} \U0001F60D.")
    elif 70 <= average_score1 < 99:
        print(f"{first_name} you got {average_score1:.2f} \U0001F60F.")
    elif average_score1 == 100:
        print(f"{first_name} you got {average_score1:.2f} \U0001F31F.")
    print(f"{first_name} {last_name} - {Exam_Name} - {custom_format}: {average_score1:,.0f}% ", file=activity_log)

    Ask_again = input("Are you finished (yes/no)? ")
    if Ask_again == 'no':
        loop = 0
    else:
        loop = 2
        average_score = (correct_answers / Count_inConnection) * 100
        print(f"{first_name} Your average score for this attempts is {average_score:,.0f}%")
        print(f"Your teacher can view  details in logs.txt.")

activity_log.close()

