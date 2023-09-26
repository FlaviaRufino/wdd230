#
print("Please enter the following: ")
print()
childrenmeal = float(input("What is the price of a child's meal? $"))
adultsmeal = float(input("What is the price of adult's meal? $"))
howmanychildren = int(input("How many children are there? "))
howmanyadults = int(input("How many adults are there? "))
salestax = float(input("What is the sales tax rate? $"))
#
print()
totalchildren = howmanychildren * childrenmeal
totaladult = howmanyadults * adultsmeal
#
print()
subtotal = round(totalchildren + totaladult, 2)
totalrate = round(subtotal * salestax / 100, 2)
total = round(subtotal + totalrate, 2)
#
print()
print(f"The Subtotal of this account is: ${subtotal}")
print(f"Salex tax is: ${totalrate}")
print(f"The total is: ${total}")
#4
print()
amount = float(input("What is the payment amount? $"))
Change = round(amount - total, 2)
print(f"The change is: ${Change}")