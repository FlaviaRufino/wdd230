# 1.- Libraries

import math

# 2.- Welcome

print('')
print('Welcome the velocity calculator. Please enter the following: ')
print('')

# 3.- Inputs
m = float(input('Mass (kg): '))
g = float(input('Gravity: '))
t = float(input('Time: '))
p = float(input('density: '))
A = float(input('cross sectional of area: '))
C = float(input('drag constant: '))

# 4.- Calculation

c = (1/2)*p*A*C
v = math.sqrt(m*g/c)*(1-math.exp((-math.sqrt(m*g*c)/m)*t))

# 5.- Outputs
print('')
print(f'The inner value of c is :{c:.3f}')
print(f'The velocity after {t} is :{v:.3f} m/s')
print('')
