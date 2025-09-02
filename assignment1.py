while True: 
    rw = int(input("Enter a number: "))
    cl = int(input("Enter a second number: "))
    srch = int(input("Search a number: "))
    
    if rw == 0 or cl == -1:
        print("Stop the loop")
        exit()
    
    for q in range(1, rw + 1):
        for w in range(1, cl + 1):
            val = q*w
            if val == srch:
                print(f"[{val}]", end="\t")
            else:
                print(val, end="\t")
        print()

#how about add a matrix just for display before search function


