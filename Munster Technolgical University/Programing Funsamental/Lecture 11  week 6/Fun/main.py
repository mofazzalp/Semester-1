# Author: Mofazzal Hossain
# Purpose:ROULETTE

import random

MIN = 0
MAX = 36
number = random.randint(MIN, MAX)
print(number)
number2 = int(input(' enter a pocket number '))  # Write a program that asks the user to enter a pocket number

if number == 0:
    print("Pocket 0 is green")
elif 1 <= number <= 18:
    if number % 2 == 0:
        print("odd-numbered pockets are red")
    else:
        print("even-numbered pockets are black")

elif 19 <= number <= 36:
    if number % 2 == 0:
        print("odd-numbered pockets are black")
    else:
        print("even-numbered pockets are red")

if number == number2:
    print("Congratulation ")
else:
    print(" better luck next time")
