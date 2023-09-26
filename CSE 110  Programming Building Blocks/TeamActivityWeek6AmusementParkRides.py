can_ride = False

age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))

is_second_rider = input("Is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))
    if height1 < 36 or height2 < 36:
        can_ride = False
    else: 
        if age1 >= 18 or age2 >= 18:
            can_ride = True
        else:
            can_ride = False
else:
     if age1 >= 18 and height1 >= 62:
        can_ride = True
     else:
         can_ride = False

if can_ride:
    print("Okay, you can ride!")
else:
    print("Sorry, you can't ride!")    