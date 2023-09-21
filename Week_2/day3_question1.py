
# Ask the user 5 bits of input: Do you want to : Show/Add/Delete/clear or Quit?
# YOUR CODE HERE

def options():
    return print('''
    Here are my services:
    [A]dd items to cart
    [V]iew cart
    [E]dit cart qty
    [D]ump everything from cart and start over
    [P]urchase cart contents
    [Q]uit
    ''')
options()

def meta_mart():
    cart = []
    while True:
        action = input("\nWhat you wanna do? ")
        if action[0].lower() == "a":
            item = input("What kind of item to put in cart? ")
            price = ord(item[0]) + ord(item[-1])
            print(f"FYI, each {item} costs ${price}")        
            while True:
                qty = input(f"How many of {item}? ")
                try:
                    qty = int(qty)
                    break
                except:
                    print("That didn't sound like a number, please try again")
            cart.append([item, qty, price])
        elif action[0].lower() == "v":
            if len(cart) == 0:
                print("it's empty!")
            for i in range(len(cart)):
                print(f"{i+1}: {cart[i][1]} {cart[i][0]} - ${cart[i][2]} each (${cart[i][1]*cart[i][2]})") 
        elif action[0].lower() == "e":
            item_list = [itm[0] for itm in cart]
            print(item_list)
            update_itm = input("Which item to edit? ")
            try:
                update_itm in item_list    
            except:
                print("I don't think you have any of those in your cart. Returing to menu")
            update_qty = input("what to change qty to? (entering 0 will remove item from cart)")
            if int(update_qty) == 0:
                print(f"{update_itm} removed from cart")
                cart.pop(item_list.index(update_itm))
            else:
                cart[item_list.index(update_itm)][1] = int(update_qty)
                print(f"{update_itm} qty changed to {update_qty}")

        elif action[0].lower() == "d":
            print("Proceeding with this option will dump everything out of your cart")
            confirm = input("Are you sure you want to do this? [Y/N]")
            if confirm[0].lower()=="y":
                cart = []
                print("Cart is now empty")
        elif action[0].lower() == "p":
            total = 0
            for itm in cart:
                total += itm[1]*itm[2]
            print(f"\n${total} has been removed from your bank account.")
            print('''
    Your item(s) are on their way.
    (don't worry, we know where you live)

    Thanks for your custom! Come again soon!
                ''')
            break
        elif action[0].lower() == "q":
            print("Bye! Come again soon!")
            break
        else:
            print("Not a valid option, please try again.")
            options()

