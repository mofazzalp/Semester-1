# Author : Mofazzal Hossain
# Description :  Assignment


import random
operators = ['+', '-']

OPTION1_CORRECT = 0

first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")

menu = f"Welcome, {first_name}" \
       "\n\t 1: Maths" \
       "\n\t 2: Irish" \
       "\n ==>"
choose = int(input(menu))
if choose == 1:
    option = int(input(f"{first_name}, how many questions? "))
    while not (5 <= option <= 25):
        option = int(input("Enter  (5 - 25)"))
        break
    for option1 in range(option):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(operators)
        if num1 > num2:
            question = f"{num1} {operator} {num2}"
        elif num2 > num1:
            question = f"{num2} {operator} {num1}"

            answer = eval(question)

            user_answer = float(input(f"What is the answer to {question}? "))

            if user_answer == answer:
                print(f"{option1+1} :{num1}{operator}{num2} = {user_answer}")
                OPTION1_CORRECT += 1
            else:
                print(f"{option1 + 1} :{num1}{operator}{num2} = {answer}")
        else:
            print("operation will ne negative answer ")
else:
    print("Unauthorised Access ")

