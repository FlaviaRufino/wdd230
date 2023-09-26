#Loops: While
tip = float(input("What is the tip amount?"))

while tip < 0:
    print("Sorry, the tip cannot be negative.")
    tip = float(input("What is the tip amount?"))
    #Jump back up to line 3

print(f'You have tipped an amount of ${tip:.2f}')