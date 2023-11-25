# Author : Mofazzal Hossain
# Description : while Looping through strings

word = 'mountain'
i = 0
count = 0
while i < len(word):
    if word[i] in 'aeiouAEIOU':
        count = count+1
        print(count)
    i = i+1

print(f"There are {count} vowels in {word}")
