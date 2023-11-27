# Author : Mofazzal Hossain
# Description :  Assignment


import random
operators = ['+', '-']

num_questions = 5  # You can change this to the desired number of questions
correct_answers = 0
questions = ''
calculation_question = 0

for circle in range(num_questions):
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
    answer = eval(calculation_question)  # Evaluate the expression to get the correct answer
    #questions = f"(calculation_question, answer))"
    questions += f"{calculation_question}, {answer}\n"
    user_answer = float(input(f"What is the result of {calculation_question}? "))

    if user_answer == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer is {answer}")

print(f"\nQuiz Summary:")
print(f"{questions}")

average_score = correct_answers / num_questions * 100
print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
print(f"Your average score is {average_score:.2f}%.")
