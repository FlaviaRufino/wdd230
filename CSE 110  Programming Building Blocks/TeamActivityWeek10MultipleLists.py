#

names    = []
balances = []

#

print("Enter the names and balances of bank accounts (type: quit when done)")
print('')
flag=True
while flag:
    name    = input("What is the name of this account? ")
    if name=='quit':
        flag=False
    else:
        balance = float(input("What is the balance? "))
        names.append(name)
        balances.append(balance)

#

print('')
print("Account Information: ")
number_items=len(names)
for k in range(number_items):
    print(f"{names[k]} - {balances[k]}")

#

print('')
total=sum(balances)
print(f"The total is: {total}")
average=total/number_items
print(f"The average is: {average:.2f}")
