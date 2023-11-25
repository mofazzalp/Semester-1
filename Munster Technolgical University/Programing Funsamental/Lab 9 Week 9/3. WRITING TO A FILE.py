# Author : Mofazzal Hossain
# Description : WRITING TO A FILE

newfile = open(input("Enter the file name "), "w")

for i in range(1, 101):
    print(i, end=" ", file=newfile)

print(" \n ", file=newfile)

for i in range(101, 201):
    print(i, end=" ", file=newfile)

newfile.close()
