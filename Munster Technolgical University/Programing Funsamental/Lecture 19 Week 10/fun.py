n = int(input("Enter an integer: "))

for outer_loop in range(0, n, 1):
    print("#", end="")
    for inner_loop in range(outer_loop + 1):
        if inner_loop == outer_loop:
            print("#", end="\n")
        else:
            print(" ", end="")
    print()  #
