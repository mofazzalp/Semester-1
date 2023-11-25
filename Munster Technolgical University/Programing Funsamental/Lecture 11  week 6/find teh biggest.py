# author : Mofazal Hossain
# description : find the biggest number

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
num3 = int(input('Enter the third number '))

if num1 > num2 and num1 > num3:
    print(f"The first Number {num1} is the biggest number")
elif num2 > num1 and num2 > num3:
    print(f"The Second Number {num2} is the biggest number")
elif num3 > num1 and num3 > num2:
    print(f"The Third Number {num3} is the biggest number")
else:
    print("Number are same ")

