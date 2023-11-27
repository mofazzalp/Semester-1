import random

operators = ['+', '-']
SPECIAL_CHARACTER_CORRECT = u'\u2713'
SPECIAL_CHARACTER_WRONG = u'\u274c'

user_option = 0
correct_answers = 0
question_no = 0
questions1 = ''
questions2 = ''

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
            calculation_question = f"{num1} {operator} {num2}"
        elif num2 > num1:
            calculation_question = f"{num2} {operator} {num1}"

        answer = eval(calculation_question)  # Evaluate the expression to get the correct answer

        # Display the question and get user's answer
        user_answer = float(input(f"{question_no} : {calculation_question} = "))

        # Check if the user's answer is correct
        if user_answer == answer:
            correct_answers += 1
            result = f"{SPECIAL_CHARACTER_CORRECT}✔️"
            print(f"{question_no} : {calculation_question} = {user_answer} {result}")
            questions1 += f"{question_no} : {calculation_question} = {user_answer} {result}\n"
        else:
            result = f"{SPECIAL_CHARACTER_WRONG}❌ should be {answer}"
            print(f"{question_no} : {calculation_question} = {user_answer} {result}")
            questions2 += f"{question_no} : {calculation_question} = {user_answer} {result}\n"

average_score = correct_answers / user_option * 100
print(f"\n{first_name}, you got {correct_answers} out of {user_option} questions correct.")
print(f"Your average score is {average_score:.2f}% 🤩")

# Print the questions and answers summary
print("\nQuestions Summary:")
print("Correct Answers:")
print(questions1)
print("Incorrect Answers:")
print(questions2)
