# BOXES

import math

# 1 - Ask the user for the integer number of manufactured items:
items = int(input("Enter a integer number of items: "))

# 2 - Ask the user for the integer number of items that the user will pack per box:
items_per_box = int(input("Enter a integer number of items per box: "))

# 3 - Compute and print the number of boxes necessary to hold the items:
num_boxes = math.ceil(items / items_per_box)

print(f"For {items}, packing {items_per_box} in each box, you will need {num_boxes} boxes. ")   

