# 01 Prove Milestone: Review Python Tire Volume

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
