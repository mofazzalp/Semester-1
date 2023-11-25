# Author : Mofazzal Hossain
# Description : EXTRA CHALLENGE
newfile = open("extra.txt", "w")
STRING_accumulator = ''
while True:
    try:
        user_input = int(input("Enter the number of people "))
        break
    except ValueError:
        print("Enter a valid integer number ")

for i in range(user_input):
    name = input(f"Enter {i + 1} person name ")
    while True:
        try:
            age = int(input(f"Enter {i + 1} person age: "))
            break
        except ValueError:
            print("Enter a valid age>>")

    STRING_accumulator += f"{name:20}, {age:10}\n"
NAME = "Name"
AGE = "Age"
person_age = 0
print(f"{NAME:28} {AGE}", file=newfile)
print(STRING_accumulator, file=newfile)
newfile.close()
with open("extra.txt", "r") as get_data:
    for i in get_data:
       i = i.rstrip()
       i = i.strip(",")
        get_name = i[0]
        get_age = int(i[1])
        print(f"{get_name} {get_age} {type(get_age)}")


### Not finished yet
