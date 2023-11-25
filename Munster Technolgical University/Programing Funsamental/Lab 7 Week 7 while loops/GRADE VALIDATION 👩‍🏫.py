# Author : Mofazzal Hossain
# Description : GRADE VALIDATION 👩‍🏫

grade = float(input("Enter Your Grade "))

while not 0 <= grade <= 100:
    grade = float(input("Enter a valid number :"))
    break
print(f"Your Number is {grade}")
