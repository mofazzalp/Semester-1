# author : Mofazzal Hossain
# purpose : entry to a professional course
# date : 25/10/23

math = int(input("Enter your Math mark "))
physics = int(input("Enter your Physics mark "))
chemistry = int(input("Enter your Chemistry mark "))
total_mark = math + physics + chemistry
total2 = math + physics
if math < 65 or physics < 55 or chemistry > 50:
    print("One of your Individual grades does not meet the threshold")
else:
    if total_mark >= 190 or total2 >= 140:
        print("Congratulation , welcome to MTU")


