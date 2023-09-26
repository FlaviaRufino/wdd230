import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            compound_dict[key] = row
    return compound_dict

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        print("Inkom Emporium\n")
        total_items = 0
        subtotal = 0.0

        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                product_num = row[0]
                quantity = int(row[1])
                if product_num in products_dict:
                    product = products_dict[product_num]
                    product_name = product[1]
                    product_price = float(product[2])
                    line_total = product_price * quantity
                    subtotal += line_total
                    total_items += quantity
                    print(f"{product_name}: {quantity} @ ${product_price:.2f} = ${line_total:.2f}")
                else:
                    print(f"Error: unknown product ID in the request.csv file\n'{product_num}'")

        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        print("\nNumber of Items:", total_items)
        print("Subtotal: $%.2f" % subtotal)
        print("Sales Tax: $%.2f" % sales_tax)
        print("Total: $%.2f" % total)

        print("\nThank you for shopping at the Inkom Emporium.")
        current_date_and_time = datetime.now()
        print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

    except FileNotFoundError:
        print("Error: missing file\n[Errno 2] No such file or directory: 'products.csv'")
    except PermissionError:
        print("Error: permission denied to access the file")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n'{e.args[0]}'")

if __name__ == '__main__':
    main()
