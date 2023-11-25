# author : Mofazzal Hossain
# description :shiopping company charges

weight = float(input("Enter a weight of package "))
SMALL_CHARGE = 1.50
MEDIUM_CHARGE = 3.00
LARGE_CHARGE = 4.00
TOTAL_COST = 0
if weight <= 2:
    TOTAL_COST = SMALL_CHARGE * weight
elif 2 < weight <= 6:
    TOTAL_COST = MEDIUM_CHARGE * weight
elif weight > 6:
    TOTAL_COST = LARGE_CHARGE * weight

print(f"The Total Cost of this shipping is {TOTAL_COST}")
