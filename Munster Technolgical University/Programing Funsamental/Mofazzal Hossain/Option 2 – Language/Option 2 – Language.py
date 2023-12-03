#first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
"""
menu = f"Welcome, {first_name}" \
       "\n\t 1: Maths" \
       "\n\t 2: Irish" \
       "\n ==> "

choose = int(input(menu))
"""
first_name = "m"
choose = 2

SPECIAL_CHARACTER_CORRECT = u'\u2713'
SPECIAL_CHARACTER_WRONG = u'\u274c'

first_average = 0
correct_answers = 0
Count_inConnection = 0
loop = 0
connection1 = ''
if choose == 2:
    while loop == 0:
        current_level = int(input(f"{first_name}, what is your current level? "))
        if current_level == 1:
            first_average += 1
            word_questions1 = ''
            connection = open("1.txt", "r")
        elif current_level == 2:
            connection = open("2.txt", "r")
            first_average += 1
            word_questions1 = ''
            for line in connection:
                Count_inConnection += 1
                line = line.strip()
                line = line.split("=")
                weekdays_count = line[0]
                weekdays = line[1]
                user_answer = input(f"{Count_inConnection}: {weekdays_count} = ")
                if user_answer == weekdays:
                    correct_answers += 1
                    word_questions1 += f"{Count_inConnection} : {weekdays_count}, = {weekdays} {SPECIAL_CHARACTER_CORRECT}\n"
                else:
                    word_questions1 += f"{Count_inConnection} : {weekdays_count}, = {user_answer} {SPECIAL_CHARACTER_WRONG} should be {weekdays}\n"
                    average_score = (correct_answers / (Count_inConnection * first_average)) * 100
                    print(average_score)
                    if 0 <= average_score < 50:
                        print(f"{first_name} you got {average_score:.2f}% \U0001F613.")
                    elif 50 <= average_score < 70:
                        print(f"{first_name} you got {average_score:.2f}% \U0001F60D.")
                    elif 70 <= average_score < 99:
                        print(f"{first_name} you got {average_score:.2f}% \U0001F60F.")
                    elif average_score == 100:
                        print(f"{first_name} you got {average_score:.2f}% \U0001F31F.")
                print(word_questions1)
                connection.close()

Ask_again = input("Are you finished (yes/no)? ")
if Ask_again == 'no':
    loop = 0
else:
    loop = 2

