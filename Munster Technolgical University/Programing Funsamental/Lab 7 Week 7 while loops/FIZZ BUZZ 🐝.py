# Author : Mofazzal Hossain
# Description : FIZZ BUZZ 🐝


i = 1
n = 100
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} fizz buzz")
    else:
        if i % 3 == 0:
            print(f"{i} word fizz")
        elif i % 5 == 0:
            print(f"{i} word buzz")
    i += 1
