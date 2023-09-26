#Loop: While

number = float(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = float(input("Please type a positive number: "))

print(f"The number is: {number}")