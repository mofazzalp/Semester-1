Ask_again = input("Are you finished (yes/no)? ")
    if Ask_again == 'no' or 'No':
        menu = f""\
           "\n\t 1: Maths" \
           "\n\t 2: Irish" \
           "\n ==> "
        choose = int(input(menu))
        if choose == 2:
            print()