# Author : Mofazzal Hossain
# Description : 3.3 if char in string.punctuation
import string
count = 0
word = input("Enter a word ")
for number in word:
    if number in string.punctuation:
        count += 1
print(count)