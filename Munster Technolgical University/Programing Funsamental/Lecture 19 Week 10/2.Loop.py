# Author : Mofazzal Hossain
# Description : Nested Loop


n = int(input("Enter an integer: "))

for outer_loop in range(0, n, 1):
    for inner_loop in range(outer_loop+1):
        print("*", end="")
    print()
