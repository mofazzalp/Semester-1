
with open("car.txt", "r") as connection:
    for line in connection:
        line = line.strip()
        line = line.split(",")
        print(line)
