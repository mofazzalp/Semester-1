# author : Mofazzal Hossain
# purpose : check features of a name
# date : 25/10/23
RESERVE_NAME = ('Julian', 'Dick', 'Anne', 'George', 'Timmy')
name = input("Enter the first name ")
if not name.isalpha():
    print("We cant accept the name, its has non-alphabetic number ")
else:
    if len(name) <= 2:
        print("The name is shorter than 2")
    elif len(name) > 8:
        print("Name is longer then 8")
    if name[0] == name[-1]:
        print("This word start and end with same letter ")
    if name in RESERVE_NAME:
        print("You are a name with one the famous five")
    else:
        print("Try another name ")

