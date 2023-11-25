# Author : Mofazzal Hossain
# Purpose : 1.writing to files


# connecting to a file

f = open("mofazzal.txt", "w")  # open(filename , access mode )

print(f"This is my string ", file=f)
print(f"Hi ", file=f)

# closing the file connection
f.close()

