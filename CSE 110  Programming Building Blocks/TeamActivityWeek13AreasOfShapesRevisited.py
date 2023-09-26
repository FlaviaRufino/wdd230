# Functions

def compute_area_square(a):
    area=a*a
    return area

def compute_area_rectangle(a,b):
    area=a*b 
    return area 

def compute_area_circle(a): 
    area=a*a*3.14 
    return area

# questions and answers

flag=True
while flag:
    print('')
    print("Enter your option, 1=square,2=rectangle,3=circle,4=quit")
    option=int(input("Enter your option: "))
    if option==1:
        print('')
        side=float(input("Enter the lenght of the side of the square: "))
        area=compute_area_square(side)
        print(f"The area of the square with side {side} is {area}.")
    elif option==2:
        print('') 
        side=float(input("Enter the lenght of the rectangle: ")) 
        sideb=float(input("Enter the width of the rectangle: ")) 
        area=compute_area_rectangle(side,sideb) 
        print(f"The area of the rectangle with lenght {side} and width {sideb} is {area}.") 
    elif option==3:
        print('') 
        side=float(input("Enter the radius of the circle: ")) 
        area=co



