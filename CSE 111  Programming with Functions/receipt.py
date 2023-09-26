import csv

from datetime import datetime

def main():
    try:
        print("Inkom Emporium\n")
        dictionary = read_products("products.csv")

        process_request("request.csv", dictionary)

        current_date_and_time = datetime.now()
        print() 
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
        print()
    
    except (FileNotFoundError, PermissionError) as ex:
        print(type(ex).__name__, ex, sep=": ")
        print("Please choose a different file.")
    except KeyError as ex:
        print(type(ex).__name__, ex, sep=": ")
        print(f"That is not a valid key.")

def read_products(filename):

    dictionary = {}

    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)

        next(reader)

        for rows in reader:
            dictionary[rows[0]] = [rows[1], rows[2]]

    return dictionary

def process_request(filename, dictionary):

    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)

        next(reader)

        num_items = 0
        subtotal = 0
        total = 0

        for rows in reader:
            key = rows[0]
            keyList = dictionary[key]
            amountOrdered = int(rows[1])
            productName = keyList[0]
            productPrice = float(keyList[1])
            print(f"{productName}: {amountOrdered} @ {productPrice}")
            subtotal += amountOrdered * productPrice
            num_items += amountOrdered
        
        print(f"\nNumber of items: {num_items}")
        print(f"Subtotal: {subtotal}")
        sales_tax = round(subtotal * 0.06, 2)
        print(f"Sales Tax: {sales_tax}")
        total = subtotal + sales_tax 
        print(f"Total: {total}")

main()