# Author : Mofazzal Hossain
# Description : calculate average

count = 0
number_sum = 0
for seq_value in range (5,22,1):
    count += 1
    number_sum += seq_value

average = number_sum/count
print(f'The average of those the number is {average}')



