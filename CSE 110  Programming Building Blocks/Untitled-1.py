meal = input("Price of the meal:  ")
tax = input("Tax (%):  ")
tip = input("Tip (%):  ")

meal = float(meal)
tax = float(tax)/100
tip = float(tip)/100

meal += meal * tax
meal += meal * tip

print("The total price you have to pay is $" + str(meal) + ".")