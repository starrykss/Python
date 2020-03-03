# 짝수, 홀수 비교

from random import random

rand = int(random() * 99) + 1
print('{} : {}'.format(rand, not bool(rand % 2)))
print('{} : {}'.format(rand, rand % 2 == 0))
