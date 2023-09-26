#Problem statement:
# In our modern world economy, many items are manufactured 
# in large factories, then packed in boxes and shipped to 
# distribution centers and retail stores. A common 
# question for employees who pack items is “How many boxes 
# do we need?”

#Import the math module so that we can call the math.ceil function.
import math

#Input from the user.
items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

# Divide the number of items per items per boxes and using math.ceil 
num_boxes = math.ceil(items / items_per_box)

# Result for the user
print(f"For {items} items, packing {items_per_box}"
f" items in each box, you will need {num_boxes} boxes.")