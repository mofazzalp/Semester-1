# Author : Mofazzal Hossain
# Description : input validation

user_name = input("Please Enter your name ")

#if len(user_name) == 0:
while len(user_name) == 0:
    print("You cant have an empty string for a name , please enter something ")
    user_name = input("Please Enter your name ")