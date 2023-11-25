# Author : Mofazzal Hossain
# Description : WORD RULES
CHECK = 'ai'
word = input("Enter a word : ")
while not word.startswith('B') or not word.endswith('g') or CHECK not in word:
    word = input("Enter a valid World : Example = Baiting >>")
print(f"Prefect")
