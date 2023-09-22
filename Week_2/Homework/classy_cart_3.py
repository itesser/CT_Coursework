from random import randint, random

class MetaMart:
    def __init__(self, name):
        self.name = name
        self.cart = []
        self.alpha_offset = randint(5,10)
        self.omega_offset = round(random(),2)
    
    def open_metamart(self):
        print(f"Welcome to Meta-Mart, {self.name}! Buy anything! Even several Moons!")
        self.shop_menu()
        while True:
            action = input("\nWhat you wanna do? ")
            if action[0].lower() == "a":
                self.add_item()
            elif action[0].lower() == "v":
                self.view_cart()
            elif action[0].lower() == "e":
                self.edit_cart()
            elif action[0].lower() == "d":
                self.dump_cart()
            elif action[0].lower() == "p":
                self.purchase()
                break
            elif action[0].lower() == "q":
                self.leave()
                break
            else:
                self.reenter()

    def shop_menu(self):
        return print('''
        Here are my services:
        [A]dd items to cart
        [V]iew cart
        [E]dit cart qty
        [D]ump everything from cart and start over
        [P]urchase cart contents
        [Q]uit
        ''')

    def add_item(self):
        item = input("What kind of item to put in cart? ")
        price = round((ord(item[0])/self.alpha_offset + ord(item[-1])/self.omega_offset)/len(item), 2)
        print(f"FYI, each {item} costs ${price}")        
        while True:
            qty = input(f"How many of {item}? ")
            try:
                qty = int(qty)
                break
            except:
                print("That didn't sound like a number, please try again")
        self.cart.append([item, qty, price])
        
    def view_cart(self):
        if len(self.cart) == 0:
            print("it's empty!")
        for i in range(len(self.cart)):
            print(f"{i+1}: {self.cart[i][1]} {self.cart[i][0]} - ${self.cart[i][2]} each (${self.cart[i][1]*self.cart[i][2]})") 

    def edit_cart(self):
        item_list = [itm[0] for itm in self.cart]
        print("currently in your cart: ")
        for thing in item_list:
            print(thing)
        update_itm = input("Which item to edit? ")
        if update_itm not in item_list:   
            print("I don't think you have any of those in your cart. Returing to menu")
            return
        else:
            update_qty = input("what to change qty to? (entering 0 will remove item from cart)")
        if int(update_qty) == 0:
            print(f"{update_itm} removed from cart")
            self.cart.pop(item_list.index(update_itm))
        else:
            self.cart[item_list.index(update_itm)][1] = int(update_qty)
            print(f"{update_itm} qty changed to {update_qty}")

    def dump_cart(self):
        print("Proceeding with this option will dump everything out of your cart")
        confirm = input("Are you sure you want to do this? [Y/N]")
        if confirm[0].lower()=="y":
            self.cart = []
            print("Cart is now empty")
    
    def purchase(self):
        total = 0
        for itm in self.cart:
            total += itm[1]*itm[2]
        print(f"\n${total} has been removed from your bank account, {self.name}.")
        print('''
Your item(s) are on their way.
(don't worry, we know where you live)

Thanks for your custom! Come again soon!
            ''')
    def leave(self):
        print(f"Bye, {self.name}! Come again soon!")

        
    def reenter(self):
        print("Not a valid option, please try again.")
        self.shop_menu()

