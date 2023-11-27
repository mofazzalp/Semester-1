# Author : Mofazzal Hossain
# Description : ASCII ACharacter


# ord('a') == chr (97)  print (a)

n = int(input("How many words do you want to translate to ASCII "))

for num in range(n):  # (range(0,stop,1) -> (0, 1, 2, 3, 4)
    word = input("Enter the word ")
    for character in word:
        print(f"\t{character} - {ord(character)}")
