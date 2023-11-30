# Author : Mofazzal Hossain
# Description : Lab 10 : 1  Reading from a file in Python

count = 0
largest_number = -100
numbers = ''

with open("numbers.txt","r") as connection:
    for line in connection:
        count += 1
        print(line)
        number = line.rstrip()
        number1 = int(line.split(' '))
        numbers += number1
        largest_number = number1
print(numbers)
print(number1)
average = number1 / count
print(average)



