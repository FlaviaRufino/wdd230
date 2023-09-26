"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# 01 CHECKPOINT REVEW PYTHON HEART RATE

# Ask for a person's age and computes and outputs the slowest and fastest rates necessary to strengthen his heart. 

persons_age = int(input("Please enter your age: "))

max_rate = 220 - persons_age
slowest = max_rate * 0.65
fastest = max_rate * 0.85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {slowest:.0f} and {fastest:.0f} per minute.")




