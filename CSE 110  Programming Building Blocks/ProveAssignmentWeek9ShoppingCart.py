print("Welcome to the Shopping Cart Program!")

print("Please select one of the following:")

products = []

shopping_cart = []

item = []

def show_options():
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def show_products():
    for p in products:
        print(["products"])


option = "1"

while option != "5":
    show_options()
    option = input("Please enter an action: ")

    if (option == "1"):
        show_options() 
        id = int(input("What item would you like to add? "))
        print("{item} has been added to the cart. ")
        shopping_cart.append({"id": id, "amount": amount})

    if (option == "2"):
        show_products = int(Input("View cart"))
        for item in shopping_cart:
            print("Products {0}".format(item[""]))
    if (option == "3"):
        option = int(input("Remove item"))
        temp = []
        for item in shopping_cart:
            if item[""]:
                temp.append(item)
    if (option == "4"): 
        for item in shopping_cart:
            if products in shopping_cart:
                sum = sum + (products["price"] * item[""])

            print("sum: {0}".format(item[""]))
            print("Compute total: ", sum)
    if (option == "5"):
        print("Quit")
        break

