"Problem Statement: You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest"
"sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%."

# Team Activity: Calling Functions - Discount

from datetime import datetime

day_of_week = datetime.now().weekday()

DISCOUNT_VALUE = 0.1
SALES_TAX = 0.06
subtotal = 0
price = -1
tuesday = 1
wednesday = 2


print()
print("||-----------------------------------------------||")
print("|| Enter the price and quantity for each item.   ||")
print("|| Type '0' if you don't want to add a new item. ||")
print("||-----------------------------------------------||")
while price != 0:
    price = float(input("Please enter the price: $"))
    if price != 0:
        quantity = float(input("Please enter quantity: "))
        subtotal = (price * quantity) + subtotal

subtotal = round(subtotal, 2)
print(f"The subtotal is: ${subtotal:.2f}")
if day_of_week == tuesday or day_of_week == wednesday:
    if subtotal >= 50.00:
        discout_amount = subtotal * DISCOUNT_VALUE
        print(f"Discount amount: $ {discout_amount:.2f}")
        subtotal = subtotal - discout_amount
    else:
        difference_for_discount = 50.00 - subtotal
        print(f"You would need to add ${difference_for_discount} in order to receive a 10% discount.")

tax_amount = subtotal * SALES_TAX
print(f"Sales tax amount: $ {tax_amount:.2f}")
total = subtotal + tax_amount

print(f"Total: ${total:.2f}")
