# Author : Mofazzal Hossain
# Description : loops continued, for loops
# Date : 13/ 11/2023

grade = -1

while 0 > grade > 100:
    try:
        grade = int(input("Enter your grade in integer "))
    except ValueError:
        grade = input("Enter your grade")
print(grade)
