# author : Mofazzal Hossain
# Purpose : Sample Exam 1


weight = float(input("Enter the weight "))

if weight > 2:
    print("Too heavy - cannot be posted")


else:
    value = float(input("Enter the total Money you Perched "))
    if 0.00 < value <= 50:
        print("Cost will be € 4.95 ")
    elif 50.01 <= value <= 100:
        print("Cost will be € 5.80")
    elif value >= 100:
        print("Cost will be €6.40")
