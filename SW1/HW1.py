# I based the conversion rate on Google's Dollar conversion on Indian Rupee's, British Pound, and Chinese Yuan
def convert(D):
    r_RATE, p_RATE, y_RATE = 88.05, 1.36, 7.12

    r = D * r_RATE
    p = D * p_RATE
    y = D * y_RATE
    
    return (r, p, y)

while True: 
    ui = (input("Enter dollar ($) (* to exit): "))
    if ui == '*':
        print("Bye")
        break
    
    D = ui.split("@")

    print(f"Dollar ($) \t Indian Rupee (R) \t British (Pound) \t China (Y)")
    for amount in D:
        D = float(amount)
        r, p, y = convert(D)
        print(f"{D} \t\t {r:.2f}\t\t{p:.2f}\t\t\t{y:.2f}")
