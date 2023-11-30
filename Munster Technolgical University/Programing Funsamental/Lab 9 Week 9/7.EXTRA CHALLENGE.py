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

    STRING_accumulator += f"{name:20},{age:10}\n"
NAME = "Name"
AGE = "Age"
oldest_age = 0
Same_AGE = ''
#print(f"{NAME:28},{AGE}", file=newfile)
print(STRING_accumulator,end="", file=newfile)
newfile.close()
with open("extra.txt", "r") as get_data:
    print(get_data)
    for line in get_data:
        line = line.rstrip()
        line = line.split(',')
        person_name = line[0]
        person_age = int(line[1])
        if person_age > oldest_age:
            oldest_age = person_age
            print(oldest_age)
        if person_age < oldest_age:
            oldest_age = person_age
            print(person_name)
        print(f"{person_name} {oldest_age} {type(oldest_age)}")
        if person_age == person_age:
            Same_AGE += f"{person_name} {person_age}"



### Not finished yet
