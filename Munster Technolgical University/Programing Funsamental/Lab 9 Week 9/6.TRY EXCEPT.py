# Author : Mofazzal Hossain
# Description : TRY/EXCEPT
DIVISION_SYMBOL = chr(247)
while True:
    try:
        x = float(input("Numerator >>>"))
        y = float(input("Denominator >>>"))
        break
    except ValueError:
        print("Enter a valid number")

try:
    division = x / y
except ZeroDivisionError:
    division = 0

print(f"{x:.2f} {DIVISION_SYMBOL} {y:.2f} = {division:.4f}")
