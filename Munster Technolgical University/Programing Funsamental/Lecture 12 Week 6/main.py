# author : Mofazzal Hossain
# purpose : write code to check e or E present
# date : 25/10/23
from typing import Tuple

latter = input("Enter a letter ")

LETTER = ('e', 'E')
if latter in LETTER:
    print("Letter is e or E")
else:
    print("Letter is not e or E")
