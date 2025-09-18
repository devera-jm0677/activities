cart = {}

mat_size = int(input("Matrix size: "))

for q in range(mat_size):
    user_item = input(f"Shopping items {q + 1}: ")
    cart[q] = user_item

print(f"\nYou have {len(cart)} items in the cart")

while True:
    user_ope = input("What would you like to do [C]hange items [R]emove [D]isplay [S]earch ? ").upper()

    if user_ope == "C":
        key = input("\nEnter key to search: ")
        if key.isdigit():
            key = int(key)
            if cart.get(key) is not None:
                print(f"Found {cart[key]} item")
                new_val = input("Enter value: ")
                cart[key] = new_val
            else:
                print("I'm sorry, not in the cart")
        else:
                print("I'm sorry, not in the cart")
    
    elif user_ope == "R":
        key = input("Enter key to search: ")
        if key.isdigit():
            key = int(key)
            if cart.get(key) is not None:
                print(f"The key {key} with value {cart[key]} has been deleted")
                cart.pop(key)
            else:
                print("Key not found")
        else:
                print("Key not found")
    
    elif user_ope == "D":
        print("\nDisplaying Values")
        print("Key\tValue")
        for key, val in cart.items():
            print(f"{key:<8} {val}")
    
    elif user_ope == "S":
        search_uitem = input("\nEnter item to search: ")
        found = False
        for key, val in cart.items():
            if val.lower() == search_uitem.lower():
                print(f"Found {val} item")
                found = True
                break
        if not found:
            print("I'm sorry, not in the cart")
    
    elif user_ope == "*":
        print("Bye")
        break

    else:
        print("Invalid choice")
