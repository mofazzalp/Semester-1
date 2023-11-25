# Author : Mofazzal Hossain
# Description : while Loop Iteration

i = 0
while i < 5:
    # Loop Iteration
    print(f"Loop Iteration {i}")

    # i = i + 1 # control variable i is update with + 1
    i = int(input("Enter a number (number greater than 5 will stop the loop): "))

print("Outside the loop")