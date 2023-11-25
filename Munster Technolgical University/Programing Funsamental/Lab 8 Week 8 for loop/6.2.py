# Author : Mofazzal Hossain
# Description : 6.2 FOR LOOP WITH CONTINUE 🔝
begin = int(input("Enter the number that you want to begin form "))
end = int(input("Enter the number that you want to end "))
for number in range(begin,end):
    if number % 8 == 0:
        print(number)


