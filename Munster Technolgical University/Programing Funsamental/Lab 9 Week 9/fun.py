# Author : Mofazzal Hossain
# Description : NESTED LOOP

user_input = 5
for i in range(user_input):
    for j in range(i):
        if i == j+1:
            print("#")
        else:
            print("",end=" ")
    print()
