# 
import random
#
number = random.randint(1, 100)
#
guess=int(input('What is the magic number? '))
while guess != number:
    if guess>number:
        print('Lower')
        guess=int(input('What is the magic number? '))
    elif guess<number:
        print('Higher')
        guess=int(input('What is the magic number? '))
    elif guess==number:
        print('You got it!')
#
print('You got it!')
print(f'The number was {number}')
