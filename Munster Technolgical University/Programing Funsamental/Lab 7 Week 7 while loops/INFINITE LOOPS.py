# Author : Mofazzal Hossain
# Description : INFINITE LOOPS

# This program demonstrates an infinite loop.
# Create a variable to control the loop.
keep_going = 'y'
n = ''
# Warning! Infinite loop!
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    # Calculate the commission.
    commission = comm_rate % sales

    # Display the commission.
    print(f'The commission is ${commission:,.2f}.')
