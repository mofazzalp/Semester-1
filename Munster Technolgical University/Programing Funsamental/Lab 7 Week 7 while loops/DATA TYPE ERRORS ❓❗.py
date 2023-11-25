# Author : Mofazzal Hossain
# Description : DATA TYPE ERRORS ❓❗

age = -1

while age < 0:
    try:
        age = int(input("Age ? "))
    except ValueError:
        print("That was not a number ")
