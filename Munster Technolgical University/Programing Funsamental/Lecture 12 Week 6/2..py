MIN_LENGTH = 2
MAX_LENGTH = 8

FAMOUS_FIVE = ("Julian", "Dick", "Anne", "George", "Timmy")

your_name = input("What is your name? ").lower()

if not your_name.isalpha():
    print("Your name should contain only letters.")
else:
    if len(your_name) < MIN_LENGTH or len(your_name) > MAX_LENGTH:
        print("Your name is not in the right range of lengths.")
    if your_name.endswith(your_name[0]):
        print("Your name starts and ends with the same letter.")
    if your_name.capitalize() in FAMOUS_FIVE:
        print("You share a name with one of the Famous Five.")