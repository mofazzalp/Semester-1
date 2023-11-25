# Author : Mofazzal Hossain
# Description : NAME VALIDATION 💬

name = input("Enter our Name : ")
while not name.isalpha():
    name = input("Enter a valid name ")
print(name)
