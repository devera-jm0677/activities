print("ASSIGNMENT 1: MULTIPLICATION TABLE")

# THE USER ENTERS A NUMBER OF ROWS AND COLUMNS
while True: 
    rw = int(input("Enter a number (Enter 0 or -1 to terminate): "))
    cl = int(input("Enter a second number (Enter 0 or -1 to terminate): "))
    
    # IF CONDITION FOR TERMINATION OF PROGRAM
    if rw == 0 or cl == -1:
        print("Stop the loop")
        exit()

    # DISPLAYS THE TABLE
    for q in range(1, rw + 1):
        for w in range(1, cl + 1):
            val = q*w
            print(val, end="\t")
        print()

    # THE USER ENTERS A NUMBER TO BE SEARCHED
    srch = int(input("Search a number: "))
    for q in range(1, rw + 1):
        # DISPLAYS THE TABLE, HIGHLIGHTING THE SEARCHED NUMBER
        for w in range(1, cl + 1):
            val = q*w
            if val == srch:
                print(f"[{val}]", end="\t")
            else:
                print(val, end="\t")
        print()
    print()

