# Author : Mofazzal Hossain
# Purpose : 4. gathering and storing information


output_file = open("Employee.txt","w")
num_employees = int(input("How many employees are there: "))

for person in range(num_employees):
    name = input(f"Enter your name {person+1}: ")
    id_number = input(f" Enter ID Number for employee {person+1} ")
    department = input(f"Enter department for employee {person+1}")

    print(f"{person+1}:{name},{id_number},{department}", file=output_file)


output_file.close()