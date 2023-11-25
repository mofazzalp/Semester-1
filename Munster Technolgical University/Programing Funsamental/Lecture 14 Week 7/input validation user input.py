# Author : Mofazzal Hossain
# Description : while input validation

grade = float(input("Enter the Grade "))

while not (0 <= grade <= 100):
    print("")
    grade = int(input("Enter Your Grade (0 - 100)"))
    break

print(f"Your grade was {grade}")