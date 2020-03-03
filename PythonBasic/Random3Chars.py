# A - Z까지 임의 문자 3자리

from random import random

a = chr(int(random() * 26) + 65)
b = chr(int(random() * 26) + 65)
c = chr(int(random() * 26) + 65)

print(a + b + c)
