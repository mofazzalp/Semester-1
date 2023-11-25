# Author : Mofazzal Hossain
# Description : LOOP FROM 1 TO 100 🔄

# 1. Write code to loop from 1 to 100, printing the number on each iteration.
i = 0
while i <= 100:
    print(i)
    i += 1

# 2. Modify the code to ask for a number n, and modify the loop to instead iterate from 1 to n instead of 1 to 100

n = int(input("Enter The number that you want to print from 1 to n "))
i = 0
while i <= n:
    print(i)
    i += 1

# 3. Add code to display the square of each number from 1 to n.

n = int(input("Enter a number that you want to print "))
i = 0
while i <= n:
    print(i**2)
    i += 1
