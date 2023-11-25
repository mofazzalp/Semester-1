# Author : Mofazzal Hossain
# Description : 1. EMAIL VALIDATION 📧
# Date : 15/11/2023

while True:
    email = input("Enter your email address: ")
    if "@" in email and email.endswith('.ie'):
        print(f"Valid email address: {email}")
        break
    else:
        print(f"Invalid email address: {email}")
