import random

num_questions = 5  # You can change this to the desired number of questions
correct_answers = 0

print("Quiz:")

for i in range(1, num_questions + 1):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)  # Evaluate the expression to get the correct answer

    user_answer = float(input(f"Question {i}: {question} = "))

    if user_answer == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer is {answer}")

average_score = correct_answers / num_questions * 100
print("\nQuiz Summary:")
print(f"You got {correct_answers} out of {num_questions} questions correct.")
print(f"Your average score is {average_score:.2f}%.")
