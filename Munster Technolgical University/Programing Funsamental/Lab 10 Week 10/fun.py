try:
    # Open the file in read mode
    with open("numbers.txt", "r") as file:
        numbers = []  # List to store the numbers
        largest_number = -100  # Initialize largest_number with negative infinity

        for line in file:
            try:
                # Convert each line to a float
                number = float(line.strip())
                numbers += f"{number}"
                if number > largest_number:
                    largest_number = number
            except ValueError:
                # Handle invalid numeric values (e.g., non-numeric lines)
                pass

        # Calculate the sum and average
        total_sum = sum(numbers)
        num_count = len(numbers)
        #average = total_sum / num_count

        print(f"Numbers read from the file: {numbers}")
        print(f"Total sum: {total_sum:.2f}")
       # print(f"Average: {average:.2f}")
        print(f"Largest number: {largest_number:.2f}")

except IOError:
    print("Error: Could not read the file 'numbers.txt'.")
