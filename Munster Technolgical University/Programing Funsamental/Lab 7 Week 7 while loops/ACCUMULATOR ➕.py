# Author : Mofazzal Hossain
# Description : ACCUMULATOR ➕

ACCUMULATOR = 0

user_input = int(input("Enter a number that you  "))
while user_input != 0:
    print(f"You Entered {user_input} ")
    ACCUMULATOR += user_input
    user_input = int(input("Enter 0 to stop the loop "))
print(f"Your Total Entered Integer umber {ACCUMULATOR}")
print("Loop Stooped")
