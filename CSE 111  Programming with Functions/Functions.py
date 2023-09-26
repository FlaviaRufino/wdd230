# Import the datetime class from datetime library
from datetime import datetime

#Print the current time 
def print_time(task_name):
    print(task_name)
    #Now I don't need the extra datetime prefix
    print(datetime.now())
    print()

first_name = "Flavia"
print("first name assigned")

print_time()

for x in range(0,10):
    print(x)
print_time("completed for loop")