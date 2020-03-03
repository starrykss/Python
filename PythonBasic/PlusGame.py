from random import random

num1 = int(random() * 90) + 10
num2 = int(random() * 90) + 10

userin = int(input('{} + {} = '.format(num1, num2)))

if userin == num1 + num2:
    print('Correct!')
else:
    print('Wrong!')