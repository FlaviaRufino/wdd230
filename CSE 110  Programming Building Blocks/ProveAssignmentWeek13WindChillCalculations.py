def retrieve_windchill(t, v):
    return round(35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16), 2)

def celsius_to_fahrenheit(t):
    return round((t * 1.8) + 32, 1)

def print_windchill(t, v):
    print(f"At temperature {t}F, and wind speed {v} mph, the windchill is: {retrieve_windchill(t, v)}F")

t = float(input("What is the temperature? "))
t_type = input("Fahrenheit or Celsius (F/C)? ")

for v in range(5, 61, 5):
    if t_type.lower() == 'c': print_windchill(celsius_to_fahrenheit(t), v)
    if t_type.lower() == 'f': print_windchill(t, v)
