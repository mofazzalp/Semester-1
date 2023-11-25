# Author : Mofazzal Hossain
# Description : 5. NESTED LOOP 🐣

user_input = int(input("Enter a number "))
for i in range(user_input+1):
    for j in range(i):
        print(i, end=" ")
    print()

