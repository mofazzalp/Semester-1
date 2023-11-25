# author : Mofazzal Hossain
# description : In operator

email_address = input("Enter your email")


if " " not in email_address and "@" in email_address:
    print("This is a valid Email")
else:
    print('This is not a valid email')