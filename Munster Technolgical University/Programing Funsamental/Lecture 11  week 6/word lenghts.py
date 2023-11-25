# author = Mofazzal Hossain
# description : shortest lengths of the word

word1 = input("Write your First word ")
word2 = input("Write Your Second Word ")
word3 = input("Write your Third Word ")
if len(word1)<len(word2) and len(word1)<len(word3):
    print(f"First word is shortest word{word1}, and its length {len(word1)}")
elif len(word2)<len(word1) and len(word2)<len(word3):
    print(f"Second  word is shortest word{word2}, and its length {len(word2)}")
elif len(word3)<len(word1) and len(word3)<len(word2):
    print(f'Third word is shortest word {word3},and its length {len(word3)}')
else:
    print("Word are same lengths ")
