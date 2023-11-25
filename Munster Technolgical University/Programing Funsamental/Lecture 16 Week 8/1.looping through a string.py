# Author : Mofazzal Hossain
# Description : looping through a string

vowel = ''
user_string = input("Enter a string ")

while len(user_string) <= 3:
    print("You show Enter a string more than 3 character ")
    user_string = input("Enter a string more that three")

for char in user_string:
    if char in 'aeiou':
        print("*", end=" ")
    elif char == ' ':
        print("@", end='')
    elif char.isdigit():
        print("X", end='')
    else:
        print(char, end="")
