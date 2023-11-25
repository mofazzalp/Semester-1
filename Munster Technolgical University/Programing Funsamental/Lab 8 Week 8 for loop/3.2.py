# Author : Mofazzal Hossain
# Description : 3. FOR LOOP STRING ITERATION 💬

COUNT = 0
char = input('Enter a sentence: ')

for i in char:
    if i.isalpha():
        COUNT += 1
print(COUNT)
