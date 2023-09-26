class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart_items = []

menu_action = None

while menu_action != 5:
    print()
    print("Please select one of the following:")
    print("1 - Add a new item")
    print("2 - View the shopping cart")
    print("3 - Remove an item")
    print("4 - Compute the total")
    print("5 - Quit")
    print()

    menu_action = int(input("Please enter an action: "))

    if menu_action == 1:
        name = input("What item would you like to add? ")
        price = float(input(f"What is the price of {name}? "))
        cart_items.append(Product(name, price))
        print(f"'{name}' has been added to the cart")
    if menu_action == 2:
        print("")
        for i, product in enumerate(cart_items):
            print(f"[{i + 1}] {product.name} ${product.price:.2f}")
    if menu_action == 3:
        index = int(input("Which item would you like to remove?: ")) - 1
        if index >= 0 and index <= len(cart_items):
            cart_items.pop(index)
            print("Item removed")
        else:
            print("Sorry, that is not a valid item number.")

    if menu_action == 4:
        total = 0
        for product in cart_items:
            total += product.price
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    
    if menu_action == 5:
        print("Your shopping cart is ready!")