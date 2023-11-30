# author : Mofazzal Hossain
#Description : Reading from a file in Python

try:
    # Read names from the file and display them
    with open("names.txt", "r") as file:
        print("Names from the file:")
        for line in file:
            name = line.strip()
            print(name)

    # Display names in uppercase
    with open("names.txt", "r") as file:
        print("\nNames in uppercase:")
        for line in file:
            name_upper = line.strip().upper()
            print(name_upper)

    # Calculate and display name lengths
    with open("names.txt", "r") as file:
        print("\nName lengths:")
        for line in file:
            name_length = len(line.strip())
            print(f"{line.strip()}: {name_length} characters")

    # Write names in lowercase to "lower.txt"
    with open("names.txt", "r") as file:
        with open("lower.txt", "w") as lower_file:
            for line in file:
                name_lower = line.strip().lower()
                print("Name in Lower case : ",name_lower)
                print(name_lower, file=lower_file)

    print("\nNames written to 'lower.txt' in lowercase.")

except FileNotFoundError:
    print("Error: The file 'names.txt' could not be found.")
