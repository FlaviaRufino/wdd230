#
choice = int(input("How many columns and rows do you want in your multiplication table?"))
#
number = choice + 1
#
for J in range(1, number):
    for I in range (1, number):
​
        multiply = J * I
        print(f"{multiply:5}", end=" ")
​
    print()