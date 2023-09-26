import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a dictionary and return the dictionary.

    Parameters:
        filename (str): The name of the CSV file to read.

    Returns:
        dict: A dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        for row in reader:
            i_number, name = row
            dictionary[i_number] = name
    return dictionary

def main():
    filename = 'students.csv'
    dictionary = read_dictionary(filename)

    i_number = input("Enter an I-Number: ")
    if i_number in dictionary:
        name = dictionary[i_number]
        print("Name:", name)
    else:
        print("No such student")

if __name__ == '__main__':
    main()
