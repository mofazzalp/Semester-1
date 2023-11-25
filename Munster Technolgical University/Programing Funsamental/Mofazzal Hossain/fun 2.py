import random

operators = ['+', '-', '*', '/']

while True:
    operator = random.choice(operators)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"{num1} {operator} {num2}"

    answer = eval(question)

    user_answer = float(input(f"What is the answer to {question}? "))

    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}.")

    another_round = input("Do you want another question? (yes/no): ")
    if another_round.lower() != 'yes':
        break
