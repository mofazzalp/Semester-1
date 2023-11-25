# Author : Mofazzal Hossain
# Description : 4. REVERSE A STRING 🔙
new = ''
n = ''
word = input("Enter a word ")
for char in word:
    new = new+char
print(new)
for i in range(len(word) -1, -1, -1):
    n = n + word[i]
print(n)

