# Author : Mofazzal Hossain
# Description : STRING ITERATOR


Punctuation_marks = ',.{}[]()'
user_sentence = input("Enter a sentence : ")

for word in user_sentence:
    if word in Punctuation_marks:
        print("X", end=" ")
    elif word == word.upper():
        print(ord(word))


