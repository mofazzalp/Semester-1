# Author : Mofazzal Hossain
# Description :  Assignment


import random

operators = ['+', '-']
SPECIAL_CHARACTER_CORRECT = u'\u2713'
SPECIAL_CHARACTER_WRONG = u'\u274c'

user_option = 0
correct_answers = 0
questions1 = ''
calculation_question = 0

loop = 1
while loop == 1:
    menu = f"Welcome," \
           "\n\t 1: Maths" \
           "\n\t 2: Irish" \
           "\n ==> "
    choose = int(input(menu))
    if choose == 1:
        print("A")

    user_ask = input("Are you finished (yes/no)? ")
    if user_ask == 'no':
        loop = 1
    else:
        loop = 2

