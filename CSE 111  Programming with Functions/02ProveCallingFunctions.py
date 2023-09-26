# 01 Prove Calling Functions

# Problem Statement:
'''Many companies wish to understand the needs and wants of their customers more deeply so the company can create products that fill
those needs and wants. One way to understand customers more deeply is to record the values entered by customers while they are using a 
program and then to analyze those values. One common way to record values is for a program to store them in a file.'''

# Second part - Prove Milestone: Tire Volume

# Import math module from the library to use math.pi
import math

# Print a introduction text and get the user input
print("Welcome, this program reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.")

# Get the users width of the tire in milimeters, aspect ratio and the diameter in inches of the wheel that the tire fits:
width = float(input("Enter the width of the tire in milimeters (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Compute and output the volume of space inside that tire:
volume = math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) /10000000000

# Print the volume result to the user: 
print(f"The approximate volume fot the tire is {volume:.2f} liters. ")

# Requirements to Prove Assingment week 01, second part:

# Open txt file
with open("volumes.txt", "at") as volumes_file:
     
    from datetime import datetime
    current_date_time = datetime.now()

    print(f"{datetime.now()},{width},{aspect_ratio},{diameter},{volume}")

print
 
