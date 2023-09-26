# 1.- Enter the numbers

print("Enter a list of numbers, type 0 when finished.")

numbers=[]

number=int(input("Enter number:"))

while number !=0:
    numbers.append(number)
    number=int(input("Enter number:"))

print(numbers)

# 2.- Calculate sum

sum_result=0
for number in numbers:
    sum_result += numbers

print(f"The sum of the numbers is:")

# 3.- Calculate average

# 4.- Calculate the largest number