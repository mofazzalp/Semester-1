# Author : Mofazzal Hossain
# Description : 3. FOR LOOP STRING ITERATION 💬

COUNT = 0
vowel = 'a', 'e', 'i', 'o', 'u'
word = []
sentence = input('Enter a sentence: ')

for i in sentence:
    if i.lower() in vowel:
        COUNT += 1
        word.append(i)
print(COUNT,"\n",word)
